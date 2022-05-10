import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class F:
    pass

for t in [None, int, float, ctypes.c_int, ctypes.CField, F]:
    try:
        S._fields_[0] = ('x', t)
    except TypeError:
        print("TypeError")
    else:
        print("no error")
