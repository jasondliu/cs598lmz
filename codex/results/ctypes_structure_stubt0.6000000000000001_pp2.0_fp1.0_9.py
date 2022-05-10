import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

f = ctypes.CDLL("./test.so")
f.foo.argtypes = [ctypes.POINTER(S)]
f.foo.restype = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print f.foo(ctypes.byref(s))
print s.x, s.y, s.z

s = S()
s.x = 1
s.y = 2
s.z = 3

print f.foo(ctypes.byref(s))
print s.x, s.y, s.z
