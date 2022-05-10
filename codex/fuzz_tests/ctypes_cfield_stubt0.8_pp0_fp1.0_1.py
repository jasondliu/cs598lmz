import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__repr__ = lambda self: '<%s>' % (self.name,)

class T(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.POINTER(ctypes.c_char)),
                ('d', ctypes.POINTER(ctypes.c_long)),
                ('e', ctypes.POINTER(ctypes.c_char_p)),
                ('f', ctypes.POINTER(ctypes.POINTER(ctypes.c_int)))]

print('fields:', T._fields_)
