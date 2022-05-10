import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CPointerType = type(S._fields_[0][1])

print 'CField:', S.x
print 'CPointerType:', S._fields_[0][1]
print 'p = CPointerType(S.x)', p = S._fields_[0][1](S.x)
print 'p.from_param(S(1))', p.from_param(S(1))
print 'p.from_param(S(1))._objects.values()', p.from_param(S(1))._objects.values()
print 'p.from_param(S(1))._objects.values()[0]', p.from_param(S(1))._objects.values()[0]
print 'p.from_param(S(1))._objects.values()[0]._objects.values()', p.from_param(S(1))._objects.values()[0]._objects.values()
print 'p.from_param(S(1))._objects.values()[0]._objects.values()[0
