import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(X.x)

# There's no public way to create a CArrayType instance, but we can
# create one by hacking the class hierarchy.
ctypes.CArrayType = type(S._fields_[0][1])

class Y(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.c_int))]

ctypes.CPointerType = type(Y.x)

class Z(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 3)]

ctypes.CArrayType = type(Z.x)

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]


