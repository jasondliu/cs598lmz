import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def CField_setattr(self, instance, value):
    if not isinstance(value, type(self)):
        value = type(self)(value)
    ctypes.c_int.__setattr__(instance, self.name, value)

ctypes.CField.__setattr__ = CField_setattr

s = S()
s.x = 5
print(s.x)
s.x = '5'
print(s.x)

s.x = 'hello'
</code>
output
<code>5
5
TypeError: unsupported operand type(s) for +: 'int' and 'str'
</code>

