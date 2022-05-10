import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@ctypes.CFuncPtr
def f(x):
    return 2 * x

print(type(f))
print(f(2))
</code>

