import ctypes
ctypes.cast(my_object, ctypes.py_object).value

# Slicing
sequence = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
sequence[3:5]
sequence[3:]
sequence[:3]
sequence[-1]
sequence[-3:]

# Comprehensions
[x*x for x in range(10)]
[(x, y) for x in range(5) for y in range(5)]
[x*x for x in range(10) if x % 2]

# ########################################################################## #
# ############################## 3 APIS #################################### #
# ########################################################################## #

# If a package contains a __init__.py file, the directory that contains it is
# treated as a package by Python.

# ############################## 3.1 Reading and Writing Files ############# #
# ########################################################################## #

# Opening Files
# Python’s built-in open() function is the preferred way to open a file.
f = open('workfile.txt', '
