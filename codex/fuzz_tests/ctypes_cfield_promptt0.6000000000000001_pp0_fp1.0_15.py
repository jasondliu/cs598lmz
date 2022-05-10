import ctypes
# Test ctypes.CField
class TestCF:
    _fields_ = [("array", ctypes.c_int * 2)]

class TestCF2:
    _fields_ = [("array", TestCF * 2)]

class TestCF3:
    _fields_ = [("array", TestCF2 * 2)]

TestCF3()

# Test ctypes.Array
ctypes.Array

ctypes.Array(ctypes.c_int, 1)

ctypes.Array(ctypes.c_int, 1, 2)

ctypes.Array(ctypes.c_int, 1, 2, 3)

ctypes.Array(ctypes.c_int, 1, 2, 3, 4)

ctypes.Array(ctypes.c_int, 1, 2, 3, 4, 5)

ctypes.Array(ctypes.c_int, 1, 2, 3, 4, 5, 6)

ctypes.Array(ctypes.c_int, 1, 2, 3, 4, 5, 6, 7)

ctypes.Array(ctypes.c_int,
