import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    c = ctypes.CField(ctypes.c_int, "a", "b")

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

# Test ctypes.CField.in_dll
assert C.c.in_dll(ctypes.CDLL(None), "a") == 0
assert C.c.in_dll(ctypes.CDLL(None), "b") == 1

# Test ctypes.CField.offset
assert C.c.offset == 0
assert D.c.offset == 2 * ctypes.sizeof(ctypes.c_int)

# Test ctypes.CField.size
assert C.c.size == 2 * ctypes.sizeof(ctypes.c_int)
assert D.c.
