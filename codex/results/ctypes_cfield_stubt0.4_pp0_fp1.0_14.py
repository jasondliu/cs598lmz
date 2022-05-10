import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def main():
    c = C()
    c.x = 1
    d = D()
    d.x = 2
    print(c.x)
    print(d.x)
    c.x = d.x
    print(c.x)

main()
