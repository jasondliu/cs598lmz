import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
This would be the closest thing to a <code>cdef</code> for <code>S.x</code> that I can think of.

