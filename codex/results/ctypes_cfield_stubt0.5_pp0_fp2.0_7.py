import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C().x)
print(type(C().x))
</code>
prints
<code>0
&lt;class 'int'&gt;
</code>

