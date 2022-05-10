from types import FunctionType
list(FunctionType(lambda x: x**2, globals())(i) for i in range(5))

# List Comprehension with if
# Program to check if a number is even
[i for i in range(10) if i % 2 == 0]

# Program to print the squares of even numbers
[i**2 for i in range(10) if i % 2 == 0]

# Program to print squares of even numbers and cubes of odd numbers
[i**2 if i % 2 == 0 else i**3 for i in range(10)]

# Program to print squares of even numbers and cubes of odd numbers
# using list comprehension
[i**2 if i % 2 == 0 else i**3 for i in range(10)]

# List Comprehension with if...else
# Program to print squares of even numbers and cubes of odd numbers
[i**2 if i % 2 == 0 else i**3 for i in range(10)]

# Program to print squares of even numbers and cubes of odd numbers
# using list comprehension
[i**2 if i % 2 == 0 else i**3 for i in range(10)]

