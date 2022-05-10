import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass

C._fields_ = [('a', ctypes.c_int), ('b', S)]

x = C()
print x.a
print x.b.x
print x.b.__class__
print C.b.__class__
print C.b.__class__.__name__

print type(C.a) is ctypes.CField
print type(C.b) is ctypes.CField

print C.a.offset
print C.b.offset
print C.b.offset + S.x.offset

import sys
if sys.platform == "win32":
    import _ctypes_test
    _ctypes_test.expect_result(C.a.offset, 0, "C.a.offset")
    _ctypes_test.expect_result(C.b.offset, 4, "C.b.offset")
    _ctypes_test.expect_result(C.b.offset + S.x.offset, 4, "C.b.offset +
