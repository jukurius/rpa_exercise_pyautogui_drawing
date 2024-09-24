# RPA Drawing with PyAutoGUI

This project automates drawing in MS Paint using PyAutoGUI. The script will open MS Paint, draw random squares on the canvas, and then create random patterns until no more squares can be detected.

## Project Structure

rpa_exercise_pyautogui_drawing/ # Source folder for the project code  
 ├── painter.py # Core drawing logic  
 ├── utils.py # Utility functions (e.g., opening/closing MS Paint, finding the canvas)  
 └── main.py # Main script to run the automation

tests/ # Unit tests  
 └── test_main.py # Tests for the main functionality

pyproject.toml # Poetry configuration file  
README.md # Project documentation file

## Prerequisites

- **Python 3.9+**
- **Poetry**

## Installation

- **poetry install**

## Run app

- **poetry run python main.py**

## Run tests

- **pytest**
