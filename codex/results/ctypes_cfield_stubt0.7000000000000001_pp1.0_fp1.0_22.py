import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test():
    print(isinstance(S.x, ctypes.CField))
    print(isinstance(S.x, int))

test()
