import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(a, b):
    return a + b

def g(a, b):
    return a + b

def h(a, b):
    return a + b

def main():
    a = S()
    a.x = 1
    a.y = 2
    a.z = 3
    b = S()
    b.x = 4
    b.y = 5
    b.z = 6
    c = S()
    c.x = 7
    c.y = 8
    c.z = 9
    d = S()
    d.x = 10
    d.y = 11
    d.z = 12
    e = S()
    e.x = 13
    e.y = 14
    e.z = 15
    f(a, b)
    g(c, d)
    h(e, a)

