import ctypes
ctypes.cast(0, ctypes.py_object).value

# A Python object is a pointer to a block of memory that contains information about the type of the object,
# the value of the object, and the reference count of the object.

# The reference count is incremented when the object is assigned to a new variable or added to a container (list, tuple, or dictionary).
# The reference count is decremented when the variable is deleted with the del statement or when the reference goes out of scope.
# When the reference count reaches zero, the memory occupied by the object is released.

# The reference count can be accessed by the sys.getrefcount function.

# The reference count is incremented by one for every reference to the object.
# Since getrefcount returns the number of references, including the reference count argument,
# we subtract one from the result.

# https://docs.python.org/3/c-api/intro.html#c.Py_IncRef

import sys
a = 37
sys.getrefcount(a)
b = a
sys.getrefcount(a)

# https://docs.python.
