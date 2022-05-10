import ctypes
ctypes.cast(0, ctypes.py_object)

# The above code will raise an exception in Python 3.
# The exception is:
# TypeError: cannot cast c_void_p instance to a pointer to other type
