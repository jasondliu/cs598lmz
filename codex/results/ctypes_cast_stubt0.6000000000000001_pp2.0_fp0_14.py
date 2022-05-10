import ctypes
ctypes.cast(0, ctypes.py_object).value
# TypeError: NULL pointer access

ctypes.cast(id(0), ctypes.py_object).value
# 0

ctypes.cast(id(None), ctypes.py_object).value
# None
</code>

