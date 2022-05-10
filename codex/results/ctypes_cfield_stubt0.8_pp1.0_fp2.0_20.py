import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('p', S)]
    _anonymous_ = ['p']

class S3(ctypes.Structure):
    pass

def main():
    print(issubclass(S2, S3))
    print(issubclass(S3, S2))

    print(issubclass(S2.p, S3))
    print(issubclass(S3, S2.p))

    print(issubclass(S2.p, ctypes.CField))
    print(issubclass(ctypes.CField, S2.p))

main()
