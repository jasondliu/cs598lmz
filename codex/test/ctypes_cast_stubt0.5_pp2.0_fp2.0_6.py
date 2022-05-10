import ctypes
ctypes.cast(ctypes.c_void_p(0x1), ctypes.c_char_p).value
# '\x01'
