import ctypes
ctypes.cast(b'\x00\x00\x00\x00\x00\x00\x00\x00', ctypes.POINTER(ctypes.c_longlong))[0]
