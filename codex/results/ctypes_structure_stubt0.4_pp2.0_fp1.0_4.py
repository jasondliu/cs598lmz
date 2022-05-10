import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class T(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
t = T()

s.x = 1
s.y = 2
s.z = 3

t.x = 1
t.y = 2
t.z = 3

print(s == t)

print(s.x == t.x)
print(s.y == t.y)
print(s.z == t.z)
</code>
which prints:
<code>False
True
True
True
</code>
So, it seems that <code>==</code> operator is not implemented for structures.

