import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [('f', ctypes.CField)]

class Y(X):
    _fields_ = [('f', ctypes.CField)]

X()
Y()
# Test ctypes.CFieldPtr
class X(ctypes.Structure):
    _fields_ = [('f', ctypes.CFieldPtr)]

class Y(X):
    _fields_ = [('f', ctypes.CFieldPtr)]

X()
Y()
# Test ctypes.CFieldArray
class X(ctypes.Structure):
    _fields_ = [('f', ctypes.CFieldArray)]

class Y(X):
    _fields_ = [('f', ctypes.CFieldArray)]

X()
Y()
# Test ctypes.CFieldPArray
class X(ctypes.Structure):
    _fields_ = [('f', ctypes.CFieldPArray)]

class Y(X):
    _fields_ = [('f', ctypes.CFieldPArray)]

X
