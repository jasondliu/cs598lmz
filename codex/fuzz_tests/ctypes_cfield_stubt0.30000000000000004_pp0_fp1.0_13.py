import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CFuncPtr = type(ctypes.CFuncPtr(None))

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CArray = type(E * 10)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CPointer = type(ctypes.pointer(F()))

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CString = type(ctypes.c_char_p(b"abc"))

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CData = type(H
