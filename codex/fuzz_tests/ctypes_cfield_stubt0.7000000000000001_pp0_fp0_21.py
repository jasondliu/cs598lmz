import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Union):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

print(C.a)
print(C.b)
print(C.c)

C.d = 9
print(C.d)

try:
    C.a = 9
except TypeError:
    print("TypeError")

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

print(C.a)
print(C.b)
print(C.c)

C.d = 9
print(C.d)

try:
    C.a = 9
except TypeError:
    print("TypeError")
