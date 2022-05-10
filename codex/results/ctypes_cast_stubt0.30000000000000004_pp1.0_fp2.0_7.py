import ctypes
ctypes.cast(0, ctypes.py_object).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.py_object).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.c_int).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.c_void_p).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.c_char_p).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.c_wchar_p).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.c_char).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.c_wchar).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.c_byte).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.c_ubyte).value

