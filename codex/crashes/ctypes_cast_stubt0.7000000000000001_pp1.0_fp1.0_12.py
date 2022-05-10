import ctypes
ctypes.cast(ctypes.pointer(ctypes.c_int(0)), ctypes.py_object).value
