import ctypes

class S(ctypes.Structure):
    x = 5
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.c_char_p)]

assert S.x == 5
assert S.a == ctypes.c_char_p
assert S.b == ctypes.c_char_p

try:
    S.c
except AttributeError:
    pass
else:
    assert False

try:
    S.x = 6
except AttributeError:
    pass
else:
    assert False


#
class XM(ctypes.Structure):
    pass

class YM(ctypes.Structure):
    _fields_ = [("x", XM)]

assert YM.x == XM

class EveryStruct(ctypes.Structure):
    pass
class EveryStructPtr(ctypes.POINTER(EveryStruct)):
    pass
