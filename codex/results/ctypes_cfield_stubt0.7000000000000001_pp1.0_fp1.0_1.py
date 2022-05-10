import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

_fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
X._fields_ = _fields_ # crashes

ctypes.CField = None
_fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
X._fields_ = _fields_ # crashes

_fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
ctypes.Structure._fields_ = _fields_ # crashes

class X(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

_fields_ = [('x', ctypes.c_int)]
X._fields_ = _fields_ # crashes

_fields_ = [('x', ctypes.c_int)]
ctypes.Union._fields_ = _fields_ # crashes
