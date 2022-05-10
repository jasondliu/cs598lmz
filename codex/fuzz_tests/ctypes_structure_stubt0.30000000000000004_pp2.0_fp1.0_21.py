import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f(x):
    return x.x

def g(x):
    return x.x

def h(x):
    return x.x

def main():
    a = S()
    a.x = 1
    b = S()
    b.x = 2
    c = S()
    c.x = 3
    d = S()
    d.x = 4
    e = S()
    e.x = 5
    f(a)
    g(b)
    h(c)
    f(d)
    g(e)
    h(a)
    f(b)
    g(c)
    h(d)
    f(e)
    g(a)
    h(b)
    f(c)
    g(d)
    h(e)
    f(a)
    g(b)
    h(c)
    f(d)
    g(e)
    h(a)
    f(b)
    g(c)
   
