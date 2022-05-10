import ctypes
ctypes.cast(0, ctypes.py_object).value

# TypeError: NULL pointer access
ctypes.cast(None, ctypes.py_object).value

# TypeError: NULL pointer access
ctypes.cast(None, ctypes.py_object)
</code>

