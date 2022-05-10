import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun4(a, b):
    return a, b
assert fun4(1, 2) == (1, 2)
try:
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, calling_convention='foo')
except ValueError:
    pass
