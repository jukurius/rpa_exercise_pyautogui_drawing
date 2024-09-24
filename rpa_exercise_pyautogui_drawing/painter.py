import pyautogui
import random
import utils


def draw_square(x: int, y: int, size: int) -> None:
    """
    Draws a square on the canvas.
    Args: x (int): x-coordinate of the square's top-left corner.
          y (int): y-coordinate of the square's top-left corner.
          size (int): size of the square's sides.
    """
    # Move the mouse to the top-left corner of the square
    pyautogui.moveTo(x, y)
    # Draw the square
    pyautogui.dragTo(x + size, y, duration=0.1)
    pyautogui.dragTo(x + size, y + size, duration=0.1)
    pyautogui.dragTo(x, y + size, duration=0.1)
    pyautogui.dragTo(x, y, duration=0.1)


def draw_random_squares_on_canvas(num_squares: int, size: int, canvas_location) -> None:
    """
    Prints random squares on the canvas.
    Calls is_overlapping to check if the squares overlap.

    args: num_squares (int): number of squares to draw.
          size (int): size of the squares.
          canvas_location (dict): dictionary with keys "left", "top", "width", "height".
    """
    left, top, width, height = (
        canvas_location["left"],
        canvas_location["top"],
        canvas_location["width"],
        canvas_location["height"],
    )
    squares = []

    while len(squares) < num_squares:
        x = random.randint(left, left + width - size)
        y = random.randint(top, top + height - size)

        if all(not utils.is_overlapping((x, y, size), sq) for sq in squares):
            draw_square(x, y, size)
            squares.append((x, y, size))
