import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass

C._fields_ = [('a', ctypes.c_int),
              ('b', ctypes.c_int)]

s = S()
s.x = 1

c = C()
c.a = 2
c.b = 3

print(s.x)
print(c.a)
print(c.b)
</code>
which outputs
<code>1
2
3
</code>

