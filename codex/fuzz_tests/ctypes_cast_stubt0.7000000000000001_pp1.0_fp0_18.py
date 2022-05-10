import ctypes
ctypes.cast(id(0), ctypes.py_object).value
# The address of the object 0 in memory.

# Python's integers are objects and they are implemented as variable-length arrays of digits some kind of linked lists.
# Those digits are stored as a character array of base 256 digits, which is 2^8 or 2^16 or 2^32 or 2^64 depending on your C implementation.

# You can check the actual implementation by looking at the source code of longobject.c in your Python's source files.

# For example, if the number sys.maxsize is 2^31 - 1, and we add one to it, we'll get -2^31.
# This is because Python uses a complement of two to store signed integers in the same way as C.

# When the number of digits gets bigger than some value, Python switches to represent the number as a C long (which could be 32 or 64 bits).

# Python's floats are also objects and they're implemented as C doubles.

# The variable-length nature of Python's numeric types comes at a cost.
# Accessing a single digit of a long integer takes linear time, which is
