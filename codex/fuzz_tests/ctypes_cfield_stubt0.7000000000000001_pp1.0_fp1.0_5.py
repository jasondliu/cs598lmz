import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

if __name__ == "__main__":
    import sys
    for field in S._fields_:
        print(field, type(field))
    print(S.x, type(S.x))
    print(S().x, type(S().x))
    print(ctypes.c_int, type(ctypes.c_int))
    print(ctypes.c_int(3), type(ctypes.c_int(3)))
