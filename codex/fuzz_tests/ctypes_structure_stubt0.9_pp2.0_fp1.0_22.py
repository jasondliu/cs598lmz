import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    foo = ctypes.c_void_p()

try:
    S.x.value = 1
except AttributeError, e:
    pass
else:
    assert False
