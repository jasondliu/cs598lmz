import ctypes
# Test ctypes.CFUNCTYPE()
def f(x, y, z):
    return x * y * z


g = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(f)
assert g(2, 3, 4) == 2 * 3 * 4

# Test ctypes.PYFUNCTYPE()
def g(x):
    return x + 1

h = ctypes.PYFUNCTYPE(ctypes.c_int)(g)
assert h(1) == 2

# Test ctypes.PY_SSIZE_T_CLEAN
assert ctypes._PY_SSIZE_T_CLEAN

# Test ctypes.Structure
class FixedSizedStructure(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]


class FlexibleSizedStructure(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("
