import ctypes
# Test ctypes.CFUNCTYPE
def func(a):
    print('func', a)

CFUNCTYPE(None, ctypes.c_int)(func)(1)

# Test ctypes.PYFUNCTYPE
def func(a):
    print('func', a)
    return a

PYFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)(1)

# Test ctypes.WINFUNCTYPE
def func(a):
    print('func', a)
    return a

WINFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)(1)

# Test ctypes.Structure
class S(Structure):
    _fields_ = [('a', ctypes.c_int)]

s = S()
s.a = 1
print(s.a)

# Test ctypes.Union
class U(Union):
    _fields_ = [('a', ctypes.c_int)]

u = U()
u.a = 1
print(u.a)

# Test
