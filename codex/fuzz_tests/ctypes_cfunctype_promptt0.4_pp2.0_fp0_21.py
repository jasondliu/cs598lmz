import ctypes
# Test ctypes.CFUNCTYPE

libc = CDLL(None)

@CFUNCTYPE(c_int, c_int, c_int)
def add(a, b):
    return a + b

assert add(2, 3) == 5

@CFUNCTYPE(c_int, c_int, c_int)
def sub(a, b):
    return a - b

assert sub(2, 3) == -1

@CFUNCTYPE(c_int, c_int, c_int)
def mul(a, b):
    return a * b

assert mul(2, 3) == 6

@CFUNCTYPE(c_int, c_int, c_int)
def div(a, b):
    return a // b

assert div(2, 3) == 0

@CFUNCTYPE(c_int, c_int, c_int)
def mod(a, b):
    return a % b

assert mod(2, 3) == 2

@CFUNCTYPE(c_int, c
