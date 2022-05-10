import ctypes
# Test ctypes.CFUNCTYPE.
def MyFunc(a, b, c):
    print a, b, c
    return a*b*c

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(MyFunc)
f(2, 3, 4)

# Test ctypes.byref.
class Struct(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]
s = Struct(1, 2, 3)
f(ctypes.byref(s))
print s.a, s.b, s.c

# Test ctypes.addressof.
f(ctypes.addressof(s))
print s.a, s.b, s.c

# Test ctypes.pointer.
p = ctypes.pointer(s)
f(p)
print s.a, s.b, s.c

#
