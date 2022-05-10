import ctypes
ctypes.cast(0, ctypes.py_object).value

# TypeError: invalid destination type for cast
ctypes.cast(None, ctypes.py_object)

# TypeError: expected integer address
ctypes.cast('hello', ctypes.py_object)
</code>

