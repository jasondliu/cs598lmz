import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(S.x)
print(S.x.__class__)
print(isinstance(S.x, ctypes.CField))
print(isinstance(S.x, ctypes.Field))
print(isinstance(S.x, ctypes.Field_))

print(S.x.offset)
print(S.x.size)
print(S.x.index)
print(S.x.pack)
print(S.x.ctype)
print(S.x.get_field_dict())
print(S.x.get_packing_as_tuple())
print(S.x.get_packing_as_dict())

print(type(S.x.offset))
print(type(S.x.size))
print(type(S.x.index))
print(type(S.x.pack))
print(type(S.x.ctype))
print(type(S.x.get_field_dict()))
print(type(S.x.get_packing_as_tuple()))
print(type(S
