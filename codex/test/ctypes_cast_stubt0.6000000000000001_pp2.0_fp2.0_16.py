import ctypes
ctypes.cast(0x12345678, ctypes.c_void_p).value

# the next line fails:
ctypes.cast(0x12345678, ctypes.c_void_p).value = 0x87654321
