import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class D(C):
    _fields_ = [('b', ctypes.c_int)]

class E(D):
    _fields_ = [('c', ctypes.c_int)]

class F(E):
    _fields_ = [('d', ctypes.c_int)]

def main():
    for base in D, E, F:
        for name in base._fields_:
            print base.__name__, name, getattr(base, name)

if __name__ == '__main__':
    main()
