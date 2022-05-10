import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyInt(int):
    pass

class MyCField(ctypes.CField):
    _type_ = ctypes.c_int

class S2(ctypes.Structure):
    _fields_ = [('x', MyCField)]

print S2.x
print S2.x._type_

class MyUnion(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

class S3(ctypes.Structure):
    _fields_ = [('x', MyUnion)]

print S3.x
print S3.x._type_

class S4(ctypes.Structure):
    _fields_ = [('x', MyInt)]

print S4.x
print S4.x._type_
