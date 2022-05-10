import ctypes
restype = ctypes.c_char_p
argtypes = ctypes.c_char_p
cfunc = ctypes.CFUNCTYPE(restype, argtypes)(6681278)
cfunc(b'Sinclair')
