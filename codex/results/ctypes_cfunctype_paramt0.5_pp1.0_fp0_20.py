import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test_func(arg):
    return arg

f = FUNTYPE(test_func)

class C(ctypes.Structure):
    _fields_ = [("func", FUNTYPE)]

c = C(f)
assert c.func(42) == 42
