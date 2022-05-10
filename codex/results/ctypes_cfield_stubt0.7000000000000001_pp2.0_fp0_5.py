import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('s', S)]

def fn(p):
    return p.x

def main():
    c = X()
    print fn(c.s)

main()
