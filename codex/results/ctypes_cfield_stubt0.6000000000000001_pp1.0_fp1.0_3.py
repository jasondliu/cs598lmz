import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

class D(C):
    def __init__(self, x):
        self.x = x

class E(object):
    pass

S.x.__set__(S(), 0)
S.x.__set__(S(), None)
S.x.__set__(S(), ctypes.c_int(0))
S.x.__set__(S(), ctypes.c_int())

try:
    S.x.__set__(S(), "")
except TypeError:
    print("TypeError")

try:
    S.x.__set__(S(), 0.0)
except TypeError:
    print("TypeError")

try:
    C.x.__set__(C(None), "")
except TypeError:
    print("TypeError")

try:
    C.x.__set__(C(None), 0.0)
except TypeError:
    print("TypeError")


