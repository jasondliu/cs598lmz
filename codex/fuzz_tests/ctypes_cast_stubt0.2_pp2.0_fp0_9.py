import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# or

ctypes.cast(id(obj), ctypes.py_object).value is obj
</code>

