import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

for i in range(100):
    fld = ctypes.CField('_%s' % i, S.x._type_)
    S._fields_.append(fld)

print(S.__dict__)
print(S.__dict__['_48'])

for i in range(100):
    print(S.__dict__['_%s' % i])
