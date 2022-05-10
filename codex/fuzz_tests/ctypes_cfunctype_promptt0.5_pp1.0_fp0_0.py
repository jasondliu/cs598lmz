import ctypes
# Test ctypes.CFUNCTYPE()

@ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)
def func(arg1, arg2):
    return "Hello %d" % arg2

print func(1, 2)
print func(1, 2, 3)
print func(1, 2, 3, 4)
print func(1, 2, 3, 4, 5)

func.restype = ctypes.c_int
print func(1, 2)
print func(1, 2, 3)
print func(1, 2, 3, 4)
print func(1, 2, 3, 4, 5)

func.argtypes = [ctypes.c_int, ctypes.c_int]
print func(1, 2)
print func(1, 2, 3)
print func(1, 2, 3, 4)
print func(1, 2, 3, 4, 5)
