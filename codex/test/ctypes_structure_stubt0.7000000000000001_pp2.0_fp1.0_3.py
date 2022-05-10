import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p

class A(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    s = S

def f():
    a = A()
    a.x = 3
    a.y = 4
    a.s.x = 5
    print(a.x)
    print(a.y)
    print(a.s.x)

f()
