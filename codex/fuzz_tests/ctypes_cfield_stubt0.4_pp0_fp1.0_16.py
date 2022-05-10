import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

s = S()
s.x = 1

c = C()
c.x = s.x

print(s.x)
print(c.x)
</code>

