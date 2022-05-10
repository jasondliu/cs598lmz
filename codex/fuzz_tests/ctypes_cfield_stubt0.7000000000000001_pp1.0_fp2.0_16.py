import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.CField):
    def __set__(self, obj, value):
        print(value)
        obj.x = value

S.x = X(ctypes.c_int)

s = S()
s.x = 5
print(s.x)
</code>
output
<code>5
5
</code>

