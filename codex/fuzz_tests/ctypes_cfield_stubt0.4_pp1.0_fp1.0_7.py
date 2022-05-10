import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', S)]

s = S(1)
c = C(s)

c.s.x = 2
print(s.x)

print(c.s.x)

c.s = S(3)
print(s.x)

print(c.s.x)

c.s = s
print(c.s.x)

c.s.x = 4
print(s.x)

print(c.s.x)
</code>
Output:
<code>2
2
1
3
2
2
4
4
</code>

