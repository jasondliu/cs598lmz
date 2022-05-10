import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __get__(self, obj, objtype):
        return obj.value
    def __set__(self, obj, value):
        obj.value = value

class S2(ctypes.Structure):
    _fields_ = [('x', CField)]

s = S2()
print s.x
s.x = 42
print s.x
</code>
Output:
<code>0
42
</code>

