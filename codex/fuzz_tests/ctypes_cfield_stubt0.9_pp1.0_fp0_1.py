import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(type(S.x))
print(type(S._fields_[0]))
print(type(S._fields_[0][0]))
print(type(S._fields_[0][1]))
print(type(S._fields_[0][1]) is S.x.__class__)
print(type(S._fields_[0]) is S.x.__class__)
print(type(S._fields_[0][0]) is S.x.__class__)
print(type(S._fields_[0]) is ctypes.CField)
print(type(S._fields_[0][0]) is ctypes.CField)
print(type(S._fields_[0]) == ctypes.CField)
try:
    print(type(S._fields_[0][0]) == ctypes.CField)
except TypeError:
    print("{} can't be compared to {}".format(S._fields_[0][0], ctypes.CField))
try:
    type(S._fields_[0][0]) ==
