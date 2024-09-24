# RPA Drawing with PyAutoGUI

This project automates drawing in MS Paint using PyAutoGUI. The script will open MS Paint, draw random squares on the canvas, and then create random patterns until no more squares can be detected.

## Project Structure

rpa_exercise_pyautogui_drawing/&nbsp;&nbsp;&nbsp;&nbsp;# Source folder for the project code  
&nbsp;&nbsp;&nbsp;&nbsp;├── painter.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Core drawing logic  
&nbsp;&nbsp;&nbsp;&nbsp;├── utils.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Utility functions (e.g., opening/closing MS Paint, finding the canvas)  
&nbsp;&nbsp;&nbsp;&nbsp;└── main.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Main script to run the automation

tests/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Unit tests  
&nbsp;&nbsp;&nbsp;&nbsp;└── test_main.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Tests for the main functionality

pyproject.toml&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Poetry configuration file  
README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Project documentation file

## Prerequisites

- **Python 3.9+**
- **Poetry**

## Installation

- **poetry install**

## Run app

- **poetry run python main.py**

## Run tests

- **pytest**
