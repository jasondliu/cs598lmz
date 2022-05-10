import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    _fields_ = [("x", ctypes.c_void_p)]

y = S.from_address(id(S))
print(y.x)
