import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class B(ctypes.CField, object):
    pass

print(B())
ctypes.create_string_buffer(S, '?')
