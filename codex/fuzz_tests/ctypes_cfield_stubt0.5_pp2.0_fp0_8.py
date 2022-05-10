import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.offset = -1

    def __repr__(self):
        return 'CField(%r, %r)' % (self.name, self.type)

print(S.x)
print(repr(S.x))
print(S.x.name)
print(S.x.type)
print(S.x.offset)

print(repr(CField('x', ctypes.c_int)))

print(S.x == CField('x', ctypes.c_int))
print(S.x == CField('y', ctypes.c_int))
print(S.x == CField('x', ctypes.c_char))
</code>
Output:
<code>CField(('x', &lt;class 'ctypes.c_int'&gt;), &lt;class 'ctypes.c_int'&gt;)
CField(
