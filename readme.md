# Hello World Application

A simple Python application demonstrating basic program structure with a greeting function and a utility for arithmetic operations.

## Features

- **Hello World Output**: A `main()` function that prints `"I am the world"` to stdout
- **Addition Utility**: An `add(a, b)` function that accepts two numbers (int or float) and returns their sum
- **Comprehensive Tests**: Full unit test coverage for both functions

## Installation

No external dependencies required. Python 3.10+ is recommended (for the `int | float` type union syntax).

```bash
# Clone or download the repository
cd helloworld

# Run the application
python main.py

# Run tests
python -m unittest test_main.py
```

## Project Structure

```
helloworld/
├── main.py        # Application entry point and utility functions
├── test_main.py   # Unit tests for main() and add()
├── plan.md        # Project plan and specification
└── readme.md      # This file
```

## Functions

### `main() -> None`
Prints the greeting string `"I am the world"` to stdout.

### `add(a: int | float, b: int | float) -> int | float`
Returns the sum of two numeric arguments. Preserves type: returns int if both args are int, otherwise float.

**Examples:**
```python
add(2, 3)      # Returns 5
add(1.5, 2.5)  # Returns 4.0
add(10, -4)    # Returns 6
```

## Testing

Run the full test suite:

```bash
python -m unittest test_main.py -v
```

The test suite includes:
- Output correctness verification
- Single-line output validation
- Return type assertions
- Edge cases (zero identity, negative numbers, floats)