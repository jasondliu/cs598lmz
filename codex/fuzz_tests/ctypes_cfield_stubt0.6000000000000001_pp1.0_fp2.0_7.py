import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(S))]

a = S()
pa = C()
pa.p = ctypes.pointer(a)

assert pa.p.contents.x == 0
pa.p.contents.x = 42
assert pa.p.contents.x == 42
pa.p.contents = a
assert pa.p.contents.x == 42

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(D))]

e = E()
e.p = ctypes.pointer(D())
assert e.p.contents.a == 0
assert e.p.contents.b == 0
e.p.contents.a = 1
e.p.contents.b = 2
assert e.p.contents.a ==
