import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    pass

C.x = ctypes.CField(S, 'x')

print(C.x)
print(C.x.__class__)
print(C.x.__class__.__bases__)

print(C.x.__get__(S(), S))
print(C.x.__get__(S(), S).__class__)
print(C.x.__get__(S(), S).__class__.__bases__)

print(C.x.__set__(S(), 42))
print(S().x)

print(C.x.__delete__(S()))
print(S().x)
</code>

