import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

CField.fget

print('S._fields_', S._fields_, S._fields_[0][1])
print('S.x', S.x, S.x.__class__)


#for field in S.__dict__.keys():
#    if isinstance(S.__dict__[field], ctypes.CField):
#        print(field, S.__dict__[field].fget(S()))

#for field, value in S._fields_:
#    print(field, value)

#print(type(S.x), type(S.y), type(S.z))
#print(dir(S.x), dir(S))

#@property
#def my_getter(s):
#    return s.x
#
#@my_getter.setter
#def my_setter(s, x):
#    s.x = x
#
#S.y = S.z
#S.x = my_getter
#S.y = my_getter
#S.y =
