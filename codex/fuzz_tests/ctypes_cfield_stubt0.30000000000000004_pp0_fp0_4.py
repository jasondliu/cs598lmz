import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

s = S()
c = C()
d = D()

print(s.x)
print(c.x)
print(d.x)

s.x = 1
c.x = 2
d.x = 3

print(s.x)
print(c.x)
print(d.x)
</code>
Output:
<code>0
0
0
1
2
3
</code>

