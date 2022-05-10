import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A:
    def __subclasshook__(self, other):
        print(other)
        return issubclass(other, ctypes.CField)

class B:
    def __subclasshook__(self, other): return other is ctypes.CField

class C:
    def __subclasshook__(self, other): return issubclass(other, ctypes.CField)

class D:
    def __subclasshook__(self, other): return other is ctypes.CField
    def __instancecheck__(self, other):
        print(other)
        return isinstance(other, ctypes.CField)

issubclass(A, ctypes.CField)
issubclass(B, ctypes.CField)
issubclass(C, ctypes.CField)
issubclass(D, ctypes.CField)

isinstance(S.x, A)
isinstance(S.x, B)
isinstance(S.x, C)
isinstance(S.x, D)
