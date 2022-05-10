import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun6(a, b, c, d, e):
    return a, b, c, d, e
assert fun6(3, 4, 5, 6, 7) == (3, 4, 5, 6, 7)
