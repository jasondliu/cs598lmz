import ctypes
ctypes.cast(pointer, ctypes.py_object).value

# or, to get a pointer to the object

ctypes.cast(pointer, ctypes.py_object).contents
</code>

