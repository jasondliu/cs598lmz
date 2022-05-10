import ctypes

class S(ctypes.Structure):
    x = 4 # field of type int

class DynS(ctypes.Structure):
    """fields of Structures may be dynamic"""
    _fields_ = [("val", ctypes.c_int)]

def test():
    print(S.x)
    print(S["x"].offset)
    print(ctypes.sizeof(S))
    print(ctypes.alignment(S))

    # vars derived
    print(S.x, repr(S.x))
    print(S.x, repr(S.x + 1))
    print(S.x, S.x + 1.0, repr(S.x + 1.0))

