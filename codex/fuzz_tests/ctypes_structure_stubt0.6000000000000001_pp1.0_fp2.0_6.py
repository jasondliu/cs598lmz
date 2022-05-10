import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong()
    _fields_ = [("y", ctypes.c_longlong), ("z", ctypes.c_int)]

p = S()
p.x = 1
p.y = 2
p.z = 3

# here, the ctypes.sizeof(S) is 16, not 24
print(ctypes.sizeof(S))

print(p.x)
print(p.y)
print(p.z)
</code>

