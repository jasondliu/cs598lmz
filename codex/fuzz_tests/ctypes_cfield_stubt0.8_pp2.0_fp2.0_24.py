import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class My_Structure(ctypes.Structure):
    _fields_ = [('x', ctypes.CField), 
                ('y', ctypes.c_int), 
                ('z', ctypes.c_int)]
</code>

