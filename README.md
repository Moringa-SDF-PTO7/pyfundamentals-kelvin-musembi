# Python Fundamentals Tasks

This code challenge demonstrates basic Python programming concepts by implementing several small functions and a class. The tasks involve writing Python functions, applying decorators, sorting data, merging dictionaries, and defining a class with attributes and methods.

## Code challenge Structure

- **Task 1: Add Numbers**: A function to add two numbers.
- **Task 2: Check Even**: A function to check if a number is even.
- **Task 3: Reverse String**: A function to reverse a string.
- **Task 4: Count Vowels**: A function to count the vowels in a string (case insensitive).
- **Task 5: Factorial Calculation**: A function to calculate the factorial of a non-negative integer.
- **Task 6: Apply Decorator**: A decorator function that prints "Decorator Applied" before executing the original function.
- **Task 7: Sort List of Tuples**: A function to sort a list of tuples by the second value (age).
- **Task 8: Merge Dictionaries**: A function to merge two dictionaries and sum the values of common keys.
- **Task 9: Car Class**: A class `Car` with attributes `make`, `model`, and `year`, and a method to display car information.

## Requirements

- Python 3.x or later
- Visual Studio Code

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Moringa-SDF-PTO7/pyfundamentals-kelvin-musembi.git
   ```

2. **Run the Python Script**

   ```bash
   python app.py
   ```

   This will run the script and print the outputs of the functions to the terminal.

## Task Details

### 1. `add_numbers(num1, num2)`

- **Description**: Adds two numbers and returns the result.
- **Usage**:

     ```python
     print(add_numbers(3, 4))  # Output: 7
     ```

### 2. `is_even(number)`

- **Description**: Returns `True` if the number is even, otherwise `False`.
- **Usage**:

     ```python
     print(is_even(10))  # Output: True
     print(is_even(9))   # Output: False
     ```

### 3. `reverse_string(text)`

- **Description**: Reverses the input string.
- **Usage**:

     ```python
     print(reverse_string('hello'))  # Output: 'olleh'
     ```

### 4. `count_vowels(text)`

- **Description**: Counts the number of vowels in a string (case insensitive).
- **Usage**:

     ```python
     print(count_vowels('Google'))  # Output: 3
     ```

### 5. `calculate_factorial(n)`

- **Description**: Returns the factorial of a non-negative integer.
- **Usage**:

     ```python
     print(calculate_factorial(5))  # Output: 120
     ```

### 6. `apply_decorator(func)`

- **Description**: A decorator that prints "Decorator Applied" before executing the original function.
- **Usage**:

     ```python
     @apply_decorator
     def example_func():
         print("Example function executed")

     example_func()
     # Output:
     # Decorator Applied
     # Example function executed
     ```

### 7. `sort_by_age(persons)`

- **Description**: Sorts a list of tuples (name, age) by the second value (age) in ascending order.
- **Usage**:

     ```python
     persons = [('Alice', 30), ('Bob', 25)]
     print(sort_by_age(persons))  # Output: [('Bob', 25), ('Alice', 30)]
     ```

### 8. `merge_dicts(dict1, dict2)`

- **Description**: Merges two dictionaries and sums values of common keys.
- **Usage**:

     ```python
     dict1 = {'a': 1, 'b': 2}
     dict2 = {'b': 3, 'c': 4}
     print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 4}
     ```

### 9. `Car` Class

- **Description**: A class representing a Car with `make`, `model`, and `year` attributes. It has a method `display_info` to print out the car's details.
- **Usage**:

     ```python
     car = Car('Toyota', 'Corolla', 2020)
     car.display_info()  # Output: Make: Toyota, Model: Corolla, Year: 2020
     ```

## Running Unit Tests

To test the functionality of all tasks, the code includes basic testing for each function in the `if __name__ == "__main__":` block. Simply run the script to see the output in the terminal.

```bash
python main.py
```

## License

This code challenge is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Explanation of the `README.md` structure

- **Introduction**: Briefly explains the code challenge.
- **code challenge Structure**: Lists the tasks and their descriptions.
- **Setup Instructions**: Guides the user on how to clone and run the script.
- **Task Details**: Provides examples of how to use each function and the expected output.
- **Running Unit Tests**: Instructs users on how to run the script to test the functions.
- **License**: MIT License.

Let me know if you need any further adjustments!
