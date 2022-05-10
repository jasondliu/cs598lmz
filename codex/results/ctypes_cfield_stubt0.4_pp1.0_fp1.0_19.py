import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.type)
print(C.x.offset)
print(C.x.size)
print(C.x.name)

print(C.x.__doc__)
print(C.x.__get__.__doc__)
print(C.x.__set__.__doc__)
print(C.x.__delete__.__doc__)

print(C.x.__get__(S(1)))
print(C.x.__get__(S(2), S))
print(C.x.__get__(S(3), int))

C.x.__set__(S(4), 5)
print(S(4).x)

C.x.__delete__(S(6))
print(S(6).x)

try:
    C.x.__set__(S(7), 'abc')
except TypeError as e:

