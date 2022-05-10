import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFunctionType(object):
    _fields_ = [('restype', ctypes.CField),
                ('argtypes', ctypes.CField * 0)]

class CFunction(object):
    _fields_ = [('__name__', ctypes.CField),
                ('__doc__', ctypes.CField),
                ('__type__', CFunctionType)]

class CType(object):
    _fields_ = [('__name__', ctypes.CField),
                ('__basicsize__', ctypes.CField),
                ('__itemsize__', ctypes.CField),
                ('__flags__', ctypes.CField),
                ('__doc__', ctypes.CField),
                ('__weakrefoffset__', ctypes.CField),
                ('__base__', ctypes.CField),
                ('__dictoffset__', ctypes.CField),
                ('__dict__', ctypes.CField),
                ('__weaklistoffset__', ctypes.CField)]

class CField(object):
    _fields_ =
