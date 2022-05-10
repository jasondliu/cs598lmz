import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("s", S)]

print(C.s.x)
print(C().s.x)
</code>
prints
<code>1
1
</code>

