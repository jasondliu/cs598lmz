import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

s = S()
print(type(s.x))
print(type(S.x))
print(S.x)
print(s.x)
print(s.x.__class__)
print(s.x.__class__ == ctypes.CField)
print(type(s.x) == ctypes.CField)
print(type(S.x) == ctypes.CField)
print(type(ctypes.CField))
print(type(ctypes.CField) == type)
print(type(type) == type)
print(type(type))
print(type(type(type)))
print(type(type(type)) == type)
print(type(type(type(type))) == type)
print(type(type(type(type))) == type)
print(type(type(type(type(type)))))
print(type(type(type(type(type)))))
print(type(type(type(type(type)))))
print(type(type(type(type(type)))))
print(type(type(type(type
