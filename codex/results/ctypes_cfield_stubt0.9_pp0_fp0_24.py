import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
It is also used not only as a <code>Structure</code> attribute type, but also inside arrays, so the field is transformed to:
<code>class S(ctypes.Structure):
    _fields_ = [('foo', ctypes.CField * 2)]
</code>
... which is unchangable in the created <code>Structure</code>.

