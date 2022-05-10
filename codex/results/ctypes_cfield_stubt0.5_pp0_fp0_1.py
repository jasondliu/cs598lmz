import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldType = type(S._fields_[0])

class C(ctypes.Structure):
    pass

class D(C):
    _fields_ = [('y', ctypes.c_int)]

s = S()
c = C()
d = D()

print(s.x)
print(type(s.x))
print(ctypes.CField)
print(type(S.x))
print(ctypes.CFieldType)
print(type(S._fields_[0]))
print(s.__dict__)
print(c.__dict__)
print(d.__dict__)
print(C.__dict__)
print(D.__dict__)
