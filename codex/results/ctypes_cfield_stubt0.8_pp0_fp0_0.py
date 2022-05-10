import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
This is not very robust. For instance, if you do <code>S._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]</code> then it will raise an exception.

