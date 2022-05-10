import ctypes
ctypes.cast(obj, ctypes.py_object).value

# Check if an object is iterable
from collections import Iterable
isinstance(obj, Iterable)

# Enumerate an iterable
list(enumerate(['a','b','c']))

# Find the most frequent value in a list
max(set(list), key=list.count)

# Check if two variables point to the same object
a is b

# Check if a value is present in a list
value in list

# Shuffle a list
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)

# Sort a dictionary by key
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted(x.items())

# Print string as error
from __future__ import print_function
print('Error: {0}'.format(e), file=sys.stderr)
