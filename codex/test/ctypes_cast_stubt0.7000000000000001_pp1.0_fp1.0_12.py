import ctypes
ctypes.cast(ctypes.pointer(ctypes.c_int(0)), ctypes.py_object).value

# ctypes.pointer(ctypes.c_int(0))
# ctypes.pointer(ctypes.c_int(0)).contents
# ctypes.pointer(ctypes.c_int(0)).contents.value
# ctypes.cast(ctypes.pointer(ctypes.c_int(0)), ctypes.py_object)
# ctypes.cast(ctypes.pointer(ctypes.c_int(0)), ctypes.py_object).value

# ctypes.pointer(ctypes.py_object(0))
# ctypes.pointer(ctypes.py_object(0)).contents
# ctypes.pointer(ctypes.py_object(0)).contents.value
# ctypes.cast(ctypes.pointer(ctypes.py_object(0)), ctypes.py_object)
# ctypes.cast(ctypes.pointer(ctypes.py_object(0)), ctypes.py_object).value

# ctypes.cast(ct
