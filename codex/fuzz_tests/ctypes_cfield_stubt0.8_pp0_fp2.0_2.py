import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
However, this might not be a good idea, depending on what you need. If you are working around an incompatibility between <code>ctypes</code> and <code>inspect</code> then you might want to look at what you are doing to see if there is a better way.

