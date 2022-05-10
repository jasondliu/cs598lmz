import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    print(ctypes.CField.__doc__)
    print()
    print(ctypes.CField.__getattribute__.__doc__)
    print()
    print(ctypes.CField.__setattr__.__doc__)
    print()
    print(ctypes.CField.__delete__.__doc__)
    print()
    print(ctypes.CField.__format__.__doc__)
    print()
    print(ctypes.CField.__init__.__doc__)
    print()
    print(ctypes.CField.__new__.__doc__)
    print()
    print(ctypes.CField.__reduce__.__doc__)
    print()
    print(ctypes.CField.__reduce_ex__.__doc__)
    print()
    print(ctypes.CField.__repr__.__doc__)
    print()
    print(ctypes.CField.__set__.__doc__)
    print()
    print(ct
