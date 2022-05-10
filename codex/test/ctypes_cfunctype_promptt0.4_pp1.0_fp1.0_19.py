import ctypes
# Test ctypes.CFUNCTYPE()

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

print(add(1, 2))
# Test ctypes.CFUNCTYPE() with restype

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

add.restype = ctypes.c_int
print(add(1, 2))
# Test ctypes.CFUNCTYPE() with argtypes

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

add.argtypes = [ctypes.c_int, ctypes.c_int]
print(add(1, 2))
# Test ctypes.CFUNCTYPE() with restype and argtypes


