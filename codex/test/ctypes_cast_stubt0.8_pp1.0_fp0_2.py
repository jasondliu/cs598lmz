import ctypes
ctypes.cast(0x12345678, ctypes.c_void_p).value

# Expected output
419712824
