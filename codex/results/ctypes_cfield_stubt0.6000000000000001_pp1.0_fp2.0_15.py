import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.CField):
    pass

class Y(ctypes.CField):
    _type_ = 'f'

class Z(ctypes.CField):
    _type_ = 'i'

class A(ctypes.Structure):
    _fields_ = [('x', X)]

class B(ctypes.Structure):
    _fields_ = [('x', Y)]

class C(ctypes.Structure):
    _fields_ = [('x', Z)]

print(A().x)
print(B().x)
print(C().x)
</code>
Output:
<code>0
0.0
0
</code>
So, the first case will set <code>_type_</code> to <code>'i'</code> (default), the second to <code>'f'</code>, and the third to <code>'i'</code> (overriding the default).

