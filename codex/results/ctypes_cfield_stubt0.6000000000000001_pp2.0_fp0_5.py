import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__module__ = ""

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

ctypes.CStructure = type(C)
ctypes.CStructure.__module__ = ""

class X(object):
    pass

x = X()

x.__class__ = ctypes.CField
print x

x.__class__ = ctypes.CStructure
print x

print ctypes.CField.__module__
print ctypes.CStructure.__module__

print ctypes.CField.__module__
print ctypes.CStructure.__module__
