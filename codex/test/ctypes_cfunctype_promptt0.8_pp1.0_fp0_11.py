import ctypes
# Test ctypes.CFUNCTYPE(*args)
func1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char, ctypes.c_char)(lambda x, y: ord(x) + y)
