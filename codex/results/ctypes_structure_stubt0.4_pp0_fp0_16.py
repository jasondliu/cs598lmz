import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

class D(ctypes.Structure):
    _fields_ = [("a", S), ("b", S)]

print D(a=(1, 2), b=(3, 4))
</code>

