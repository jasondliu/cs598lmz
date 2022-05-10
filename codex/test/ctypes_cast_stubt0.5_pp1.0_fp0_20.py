import ctypes
ctypes.cast(id(int), ctypes.py_object).value

# this is the same as the previous line
ctypes.cast(id(int), ctypes.c_void_p).value

# this is the same as the previous line
