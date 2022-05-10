import ctypes

class S(ctypes.Structure):
    x = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

s = S()
s.x = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
assert s.x(42) == 42

class M(ctypes.Structure):
    _fields_ = [("x", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))]

m = M()
m.x = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
assert m.x(42) == 42

# cannot assign callable directly
try:
    x = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    x = lambda x: x
except TypeError:
    pass
