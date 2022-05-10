import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

obj = S()
print(type(S.x)) # <class 'ctypes.c_long'>
print(obj.x) # 0

obj.x = 5
print(obj.x) # 5

print('x' in C._fields_) # True
print(type(C._fields_[0])) # <class 'ctypes.CField'>
print(C._fields_[0][0]) # 'x'

print(C._fields_[0][1]) # <class 'ctypes.c_long'>

print(C._fields_[1][0]) # 'y'
print(C._fields_[1][1]) # <class 'ctypes.c_long'>
