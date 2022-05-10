import ctypes
ctypes.cast(obj, ctypes.py_object).value

# Tuple

# Empty
t = ()

# Single item
t = (1,)

# Multiple items
t = (1, 2, 3, 4, 5)

# Accessing elements
t[0]
t[-1]

# Slicing
t[1:3]

# Concatenation
t + (6, 7, 8)

# Repetition
t * 3

# Immutable

# Unpacking

# Swapping variables
a, b = 1, 2
a, b = b, a

# Iterating
for x in t:
    print(x)

# Tuple as return value
def min_max(t):
    return min(t), max(t)

# Tuple as argument
def print_all(*args):
    for x in args:
        print(x)

# List

# Empty
l = []

# Single item
l = [1]

# Multiple items
l = [1, 2, 3, 4, 5]
