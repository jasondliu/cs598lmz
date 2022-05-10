import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

type.__init__(ctypes.CField, 'CField', (object, ), {})
