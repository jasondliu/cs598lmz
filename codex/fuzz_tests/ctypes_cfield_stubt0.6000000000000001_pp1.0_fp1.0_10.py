import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __repr__(self):
        return 'CField(%r, %r)' % (self._name_, self._type_)

def patch_cfield():
    ctypes.CField = CField

patch_cfield()

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_char)]

print(S.x)
print(S.y)

del S.x
print(S.y)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_char)]

print(S.x)
print(S.y)

del S.x
print(S.y)
