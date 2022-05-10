import ctypes
# Test ctypes.CFUNCTYPE()

# This one works:
#func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)

# This one gives a segfault:
func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)

print(func(7))
