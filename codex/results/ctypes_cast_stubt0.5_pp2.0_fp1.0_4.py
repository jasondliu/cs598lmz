import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# what is the difference between
# ctypes.cast(id(obj), ctypes.py_object).value
# and
# obj
