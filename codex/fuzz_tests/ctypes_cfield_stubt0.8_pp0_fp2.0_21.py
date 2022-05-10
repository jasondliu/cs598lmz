import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
<code>type(S.x)</code> is the type of the <code>x</code> attribute of a <code>S</code> instance, a <code>ctypes.Field</code> object.

