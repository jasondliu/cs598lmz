import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
The line <code>ctypes.CField = ...</code> is analogous to <code>ctypes.Structure.CField = ...</code>, but the latter is actually an alias for <code>ctypes.c_int</code>.

