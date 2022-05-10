import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', ctypes.CField)]

c = C()
c.s.x = 1
c.s.x += 1

import _testcapi
assert _testcapi.getargs_CField(c.s.x) == (2,)
assert _testcapi.getargs_CField(c.s) == (2,)
assert _testcapi.getargs_CField(c) == (2,)

class D(ctypes.Structure):
    _fields_ = [('s', ctypes.CField)]

d = D()
d.s.x = 1
d.s.x += 1

assert _testcapi.getargs_CField(d.s.x) == (2,)
assert _testcapi.getargs_CField(d.s) == (2,)
assert _testcapi.getargs_CField(d) == (2,)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes
