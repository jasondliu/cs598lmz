import ctypes
ctypes.cast(my_str, ctypes.py_object).value

# If you are using Python 3.x, use this instead:
# ctypes.cast(my_str, ctypes.py_object).value
</code>

