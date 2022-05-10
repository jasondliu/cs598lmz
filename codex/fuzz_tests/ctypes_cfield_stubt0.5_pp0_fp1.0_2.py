import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.CField))]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.POINTER(ctypes.CField)))]

print(type(S.x))
print(type(C.x))
print(type(D.x))
print(type(E.x))
print(type(F.x))
print(type(F.x.contents))
print(type(F.x.contents.contents))

try:
    type(F.x.contents.contents.contents)
except:
    print("F.x.contents.contents.contents raises exception")

print(type(C.x.
