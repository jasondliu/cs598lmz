import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class B(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f_impl(x):
    return x+1

def g_impl(x):
    return x+1

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(S))(f_impl)
g = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(B))(g_impl)

s = S()
s.x = 1
s.y = 2

b = B()
b.x = 3
b.y = 4

print f(ctypes.byref(s))
print g(ctypes.byref(b))
print f(ctypes.byref(b))
print g(ctypes.byref(s))
</code>

