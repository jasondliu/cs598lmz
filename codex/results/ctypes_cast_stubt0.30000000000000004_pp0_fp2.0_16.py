import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is the only way to access the value of a NULL pointer.
# Note that it's written in C, not Python, so it doesn't follow
# Python's normal rules for what an expression does.
# In particular, it doesn't set an exception if it receives a NULL
# pointer; it just returns NULL.

# The expression (ctypes.py_object).value is a type.  It's the type
# of the .value attribute of ctypes objects that represent Python
# objects.

# The expression ctypes.cast(0, ctypes.py_object) creates a
# ctypes object of type ctypes.py_object.  The value of this
# object is NULL.

# The expression ctypes.cast(0, ctypes.py_object).value then
# fetches the .value attribute of this object, which is NULL.

# So this expression is equivalent to "return NULL".

# The rest of this file shows what happens if you try to use other
# expressions.

# If you try to use "return 0", Python raises an
