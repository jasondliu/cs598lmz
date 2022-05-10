import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [("s", S)]

s = S()
t = T()
t.s = s

print(t.s.x)
print(s.x)

t.s.x = 42
print(t.s.x)
print(s.x)
</code>
Output:
<code>0
0
42
42
</code>

