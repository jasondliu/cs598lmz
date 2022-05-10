import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(D):
    _fields_ = [('z', ctypes.c_int)]

def main():
    print(D.x)
    print(E.x)
    print(E.y)
    print(E.z)

if __name__ == "__main__":
    main()
