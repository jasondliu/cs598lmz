import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.Field = type(S._fields_[0])
</code>

Note that in your example, <code>type(S)</code> is <code>type</code>, and <code>type(S.x)</code> is <code>int</code> (or at least <code>int</code> in 3.x; in 2.x it might be <code>ctypes.c_int</code> or something).

