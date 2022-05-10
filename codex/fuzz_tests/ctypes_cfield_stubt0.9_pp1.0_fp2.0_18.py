import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(S.x)
print(type(S.x))

# the CField class is actually a little different, but the above is how
# it's exposed in the ctypes module

try:
    S.x = 3 # can't reassign x because S.x is a ctypes.CField
except TypeError:
    print('TypeError')

class MyCField(ctypes.CField):
    pass

print(type(MyCField))
print(MyCField)

print(type(ctypes.py_object))
print(ctypes.py_object)
