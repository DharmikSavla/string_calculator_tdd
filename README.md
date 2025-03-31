# String Calculator TDD

## Project Overview
This project showcases TDD (Test Driven Development) by a simple string calculator.
Test-Driven Development (TDD) is a software development approach where you write tests before writing the code, following a cycle of writing a failing test, writing the code to make it pass and then refactoring.

## Features

- Parses input numbers from a string and returns their sum.
- Supports comma (,) and newline (\n) delimiters by default.
- Handles an unknown amount of numbers as input.
- Allows custom delimiters specified in the format //[delimiter]\n[numbers].
- Uses regular expressions (re.split) to handle complex delimiters efficiently.
- Exception handling for invalid inputs and format errors.

## Setup and Testing

### 1. Set up a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 2. Testing
```sh
python -m unittest test_string_calculator.py

*****   Thank You!    *****