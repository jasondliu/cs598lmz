import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.CField, 'x')]

value = 123
S.x.set(S(value), 42)
print(value)
</code>
Output:
<code>42
</code>

