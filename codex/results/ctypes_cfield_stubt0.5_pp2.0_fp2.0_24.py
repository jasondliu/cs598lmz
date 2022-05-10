import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

assert C._fields_[0] is S.x

C._fields_ = [('x', ctypes.c_int)]

assert C._fields_[0] is not S.x

assert issubclass(C, S)

assert C.x is not S.x

assert C.x.offset == S.x.offset
assert C.x.size == S.x.size
assert C.x.name == S.x.name
assert C.x.ctype is ctypes.c_int

import _ctypes_test

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

assert C._fields_[0] is not S.x

assert issubclass(C, S)

assert C.x is not S.x

assert C.x.offset == S.x.offset
assert C.x.size == S.x.size
assert C.x
