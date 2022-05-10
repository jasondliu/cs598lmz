import ctypes
ctypes.cast(0, ctypes.py_object).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.py_object).value

# TypeError: NULL pointer access
# ctypes.cast(None, ctypes.c_int).value

# ctypes.cast(0, ctypes.c_int).value
# 0

# ctypes.cast(0, ctypes.c_void_p).value
# 0

# ctypes.cast(0, ctypes.c_char_p).value
# b'\x00'

# ctypes.cast(0, ctypes.c_char_p).value.decode()
# ''

# ctypes.cast(0, ctypes.c_char_p).value.decode('ascii')
# ''

# ctypes.cast(0, ctypes.c_char_p).value.decode('ascii', 'ignore')
# ''

# ctypes.cast(0, ctypes.c_char_p).value.decode('ascii', '
