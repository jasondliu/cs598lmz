import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

ctypes.CStructure = type(C)

class D(ctypes.CStructure):
    _fields_ = [('x', ctypes.CField)]

print(type(D.x) is ctypes.CField)
print(type(D) is ctypes.CStructure)

class E(ctypes.CStructure):
    _fields_ = [('x', ctypes.CField)]
    _pack_ = 1

print(type(E.x) is ctypes.CField)
print(type(E) is ctypes.CStructure)

class F(ctypes.CStructure):
    _fields_ = [('x', ctypes.CField)]
    _pack_ = 1
    _abstract_ = True

print(type(F.x) is ctypes.CField)
print(type(F) is ctypes.CStructure)

class G(ctypes.CStructure):

