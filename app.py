# Task 1: Adds two numbers and returns the result
def add_numbers(num1, num2):
    """Returns the sum of two numbers"""
    return num1 + num2

# Task 2: Checks if a number is even
def is_even(number):
    """Returns True if the number is even, otherwise False"""
    return number % 2 == 0

# Task 3: Reverses the input string
def reverse_string(text):
    """Returns the reversed version of the input string"""
    return text[::-1]

# Task 4: Counts the number of vowels in a string (case insensitive)
def count_vowels(text):
    """Returns the count of vowels (a, e, i, o, u) in the input string, ignoring case"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# Task 5: Computes the factorial of a number
def calculate_factorial(n):
    """Returns the factorial of a non-negative integer"""
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Task 6: Applies a decorator that prints "Decorator Applied" before calling the original function
def apply_decorator(func):
    """Decorator function that adds a print statement before function execution"""
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

# Example of using apply_decorator
@apply_decorator
def example_func():
    """An example function to demonstrate the decorator"""
    print("Example function executed")

# Task 7: Sorts a list of tuples by the second value (age)
def sort_by_age(persons):
    """Returns a list of tuples sorted by age in ascending order"""
    return sorted(persons, key=lambda x: x[1])

# Task 8: Merges two dictionaries and sums values of common keys
def merge_dicts(dict1, dict2):
    """Merges two dictionaries. If a key exists in both, sums their values."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

# Task 9: Car class with attributes make, model, and year, and a method to display info
class Car:
    """Represents a Car object with make, model, and year attributes"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Displays car information in a formatted string"""
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Unit tests to test all tasks functionalities
if __name__ == "__main__":
    # Test Task 1
    print(add_numbers(3, 4))  # Output: 7
    
    # Test Task 2
    print(is_even(10))  # Output: True
    print(is_even(9))   # Output: False

    # Test Task 3
    print(reverse_string('hello'))  # Output: 'olleh'

    # Test Task 4
    print(count_vowels('Google'))  # Output: 3

    # Test Task 5
    print(calculate_factorial(5))  # Output: 120

    # Test Task 6
    example_func()  # Output: Decorator Applied, Example function executed

    # Test Task 7
    persons = [('Alice', 30), ('Bob', 25)]
    print(sort_by_age(persons))  # Output: [('Bob', 25), ('Alice', 30)]

    # Test Task 8
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 4}

    # Test Task 9
    car = Car('Toyota', 'Corolla', 2020)
    car.display_info()  # Output: Make: Toyota, Model: Corolla, Year: 2020
