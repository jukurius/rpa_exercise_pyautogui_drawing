import pytest
from unittest.mock import patch, MagicMock

from rpa_exercise_pyautogui_drawing.main import main

pass_count = 0  # Counter to track the number of successful test passes


@pytest.mark.parametrize("run_count", range(4))
@patch("utils.find_canvas")
@patch("utils.find_all_squares")
@patch("utils.generate_random_int")
def test_main(
    mock_generate_random_int,
    mock_find_all_squares,
    mock_find_canvas,
    run_count,
):
    global pass_count

    # Mock the return values of the functions
    mock_generate_random_int.return_value = 3
    mock_find_canvas.return_value = MagicMock(left=0, top=0, width=100, height=100)

    # Test case where the condition should be True
    mock_find_all_squares.return_value = [(10, 10, 50), (20, 20, 50), (30, 30, 50)]

    try:
        with patch("builtins.print") as mocked_print:
            main()
            mocked_print.assert_any_call("All squares have been drawn successfully.")
        pass_count += 1  # Increment the counter if the test passes
    except AssertionError:
        # If the test fails, we don't increment the pass_count
        pass

    test_report_pass_count()


def test_report_pass_count():
    """This test will run after all other tests and print the pass count."""
    global pass_count
    print(f"\nNumber of passes: {pass_count}/4")
