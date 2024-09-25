import random
import pyautogui
import time
import pygetwindow as gw
import logging
from typing import Union, Dict

# Constants
CANVAS_SAMPLE_PATH = "canvas_sample.png"
SQUARE_SAMPLE_PATH = "square_sample.png"
DEFAULT_CANVAS_SIZE = (800, 600)
MIN_CONFIDENCE = 0.5
MAX_CONFIDENCE = 0.887
CONFIDENCE_REDUCER = 0.01
WAIT_TIME = 1  # Default wait time between actions

# Logger setup
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def open_paint() -> None:
    """Opens the MS Paint application."""
    try:
        pyautogui.hotkey("win", "r")
        pyautogui.typewrite("mspaint")
        pyautogui.press("enter")
        wait_until_window_opens("Paint")
        set_canvas_size(*DEFAULT_CANVAS_SIZE)
        pyautogui.hotkey("p")  # Set the pen tool
    except Exception as e:
        logging.error(f"Error opening Paint: {e}")
        raise e


def close_paint() -> None:
    """Close the MS Paint application if it is open."""
    try:
        paint_windows = [
            window for window in gw.getAllWindows() if "Paint" in window.title
        ]
        if paint_windows:
            for window in paint_windows:
                window.activate()
                pyautogui.hotkey("alt", "f4")
                pyautogui.press("tab")  # Choose not to save changes
                pyautogui.press("enter")
            logging.info("MS Paint has been closed.")
        else:
            logging.warning("MS Paint is not open.")
    except Exception as e:
        logging.error(f"Error closing Paint: {e}")
        raise e


def set_canvas_size(width: int, height: int) -> None:
    """Set the canvas size in MS Paint."""
    try:
        pyautogui.hotkey("ctrl", "e")
        time.sleep(WAIT_TIME)
        pyautogui.typewrite(str(width))
        pyautogui.press("tab")
        pyautogui.typewrite(str(height))
        pyautogui.press("enter")
        time.sleep(WAIT_TIME)
    except Exception as e:
        logging.error(f"Error setting canvas size: {e}")
        raise e


def find_canvas() -> Union[Dict[str, int]]:
    """Find the canvas area in MS Paint."""
    try:
        canvas_location = pyautogui.locateCenterOnScreen(
            CANVAS_SAMPLE_PATH, confidence=MAX_CONFIDENCE
        )
        if canvas_location:
            canvas_size = pyautogui.locateOnScreen(
                CANVAS_SAMPLE_PATH, confidence=MAX_CONFIDENCE
            )
            if canvas_size:
                return {
                    "left": canvas_location.x + 180,
                    "top": canvas_location.y,
                    "width": canvas_size.width,
                    "height": canvas_size.height,
                }
        logging.warning("Canvas not found.")
        return None
    except pyautogui.ImageNotFoundException:
        logging.error("Canvas sample image not found.")
        raise e
    except Exception as e:
        logging.error(f"Error locating canvas: {e}")
        raise e


def find_all_squares(square_count: int) -> Union[list, None]:
    """
    Find all squares on the canvas.
    Confidence decreases incrementally until the required number of squares are found.
    """
    confidence = MAX_CONFIDENCE
    squares = list(
        pyautogui.locateAllOnScreen(SQUARE_SAMPLE_PATH, confidence=confidence)
    )

    while len(squares) < square_count and confidence >= MIN_CONFIDENCE:
        confidence -= CONFIDENCE_REDUCER
        logging.info(f"Reducing confidence to {confidence}")
        squares = list(
            pyautogui.locateAllOnScreen(SQUARE_SAMPLE_PATH, confidence=confidence)
        )

    if len(squares) >= square_count:
        return squares
    else:
        logging.warning(f"Expected {square_count} squares but found {len(squares)}")
        return None


def check_if_squares_are_messed_up() -> list:
    """Check if the squares on the canvas are messed up."""
    try:
        squares = list(pyautogui.locateAllOnScreen(SQUARE_SAMPLE_PATH, confidence=0.7))
        return squares if squares else []
    except Exception as e:
        logging.error(f"Error locating squares: {e}")
        return []


def draw_random_mess(canvas_location: Dict[str, int]) -> None:
    """Draw random lines on the Paint canvas until the squares can't be recognized."""
    left, top, width, height = canvas_location.values()
    squares = check_if_squares_are_messed_up()

    while squares:
        start_x, start_y = random.randint(left, left + width), random.randint(
            top, top + height
        )
        end_x, end_y = random.randint(left, left + width), random.randint(
            top, top + height
        )

        pyautogui.moveTo(start_x, start_y)
        pyautogui.dragTo(end_x, end_y)

        squares = check_if_squares_are_messed_up()
        if len(squares) == 1:
            break


def generate_random_int(min_val: int, max_val: int) -> int:
    """Generate a random integer between min_val and max_val."""
    return random.randint(min_val, max_val)


def is_overlapping(square1, square2) -> bool:
    """Check if two squares are overlapping."""
    x1, y1, size1 = square1
    x2, y2, size2 = square2

    return not (
        x1 + size1 <= x2 or x2 + size2 <= x1 or y1 + size1 <= y2 or y2 + size2 <= y1
    )


def wait_until_window_opens(window_name: str, timeout=10) -> bool:
    """Wait until a window with the specified name is opened."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if any(window for window in gw.getAllWindows() if window_name in window.title):
            return True
        time.sleep(0.5)
    logging.error(f"Window '{window_name}' did not open within {timeout} seconds.")
    return False
