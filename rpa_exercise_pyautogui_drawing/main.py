import logging
from painter import draw_random_squares_on_canvas
from utils import (
    open_paint,
    close_paint,
    generate_random_int,
    find_canvas,
    find_all_squares,
    draw_random_mess,
)

# Constants
SQUARE_COUNT_MIN = 2
SQUARE_COUNT_MAX = 5
SQUARE_SIZE = 50

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def initialize_paint_and_canvas():
    """Open Paint and locate the canvas."""
    try:
        open_paint()
        canvas_location = find_canvas()
        if not canvas_location:
            raise RuntimeError("Canvas could not be found.")
        return canvas_location
    except FileNotFoundError as e:
        logging.error("Canvas sample image not found.")
        close_paint()
        raise e
    except Exception as e:
        logging.error(f"Error initializing Paint or locating canvas: {e}")
        close_paint()
        raise e


def draw_squares_and_validate(canvas_location, square_count):
    """Draw squares on the canvas and validate the count."""
    try:
        draw_random_squares_on_canvas(
            square_count, size=SQUARE_SIZE, canvas_location=canvas_location
        )
        squares = find_all_squares(square_count)

        if squares and len(squares) == square_count:
            logging.info("All squares have been drawn successfully.")
            return True
        else:
            logging.warning(
                f"Square count mismatch: Found {len(squares)} squares, expected {square_count}."
            )
            return False
    except Exception as e:
        logging.error(f"Error drawing squares or validating: {e}")
        return False


def main() -> None:
    square_count = generate_random_int(SQUARE_COUNT_MIN, SQUARE_COUNT_MAX)
    logging.info(f"Starting to draw {square_count} squares.")

    try:
        canvas_location = initialize_paint_and_canvas()

        # Draw squares and validate
        if draw_squares_and_validate(canvas_location, square_count):
            # draw random lines to mess up the canvas
            draw_random_mess(canvas_location)

    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")
    finally:
        close_paint()


if __name__ == "__main__":
    main()
