import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldPtr = type(ctypes.pointer(S.x))
ctypes.CFieldArray = type(S.x * 2)

class C(ctypes.Structure):
    _fields_ = [('s', S)]

class D(ctypes.Union):
    _fields_ = [('s', S)]

x = C()
print type(x.s) == S
print type(x.s) == ctypes.CField
print isinstance(x.s, S)
print isinstance(x.s, ctypes.CField)
print isinstance(x.s, ctypes.CFieldPtr)
print isinstance(x.s, ctypes.CFieldArray)

y = D()
print type(y.s) == S
print type(y.s) == ctypes.CField
print isinstance(y.s, S)
print isinstance(y.s, ctypes.CField)
print isinstance(y.s, ctypes.CFieldPtr)
print isinstance(y.s, ctypes.CFieldArray
