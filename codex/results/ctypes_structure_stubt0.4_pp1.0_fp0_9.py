import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int)]

def f():
    return S()

def g():
    return S(1)

print f()
print g()

def h():
    return S(1, 2)

print h()
</code>

