import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f():
    s = S()
    s.x = 42
    return s

def g():
    s = f()
    return s

def h():
    s = g()
    return s

s = h()
print s.x
</code>

