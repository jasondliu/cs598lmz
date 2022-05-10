import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

add(1, 2)

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

add(1, 2)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add(a, b, c):
    return a + b + c

add(1, 2, 3)
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.
