import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

def f():
    return S().x

def g():
    return C().y

def h():
    return C().y + 1

def main():
    for x in range(10000):
        f()
        g()
        h()

main()
