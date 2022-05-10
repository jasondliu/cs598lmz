import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

import _ctypes

assert _ctypes.PyObj_FromPtr is not None
assert _ctypes.PyCObject_AsVoidPtr is not None
assert _ctypes.PyCObject_FromVoidPtrAndDesc is not None
