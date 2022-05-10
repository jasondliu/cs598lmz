import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32 
    y = ctypes.c_int32

lib.foo.argtypes = [ctypes.POINTER(S)]
lib.foo.restype = ctypes.c_int32

s = S()
s.x = 5
s.y = 7
print lib.foo(s)
</code>

