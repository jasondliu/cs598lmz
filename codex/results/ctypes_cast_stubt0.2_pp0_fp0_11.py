import ctypes
ctypes.cast(ctypes.c_void_p(0x12345678), ctypes.c_char_p).value

# ctypes.cast(ctypes.c_void_p(0x12345678), ctypes.c_char_p).value
# 'xE7'
</code>

