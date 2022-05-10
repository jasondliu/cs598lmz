import ctypes
# Test ctypes.CFUNCTYPE
class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

def f(x):
    return x.x

F = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(X))
f1 = F(f)

x = X()
x.x = 42
print(f1(x))

# Test ctypes.WINFUNCTYPE
def f(x):
    return x.x

