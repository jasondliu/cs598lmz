import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.CField)]

class Z(ctypes.Structure):
    _fields_ = [("c", Y)]

class W(ctypes.Structure):
    _fields_ = [("d", Z)]

x = X()
x.a = 1

w = W()
w.d.c.b = x

# w.d.c.b should be the same as x
assert w.d.c.b.a == x.a
assert w.d.c.b.a == 1

# x.a should be the same as w.d.c.b.a
assert x.a == w.d.c.b.a
assert x.a == 1

# x.a should be the same as w.d.c.b.a
assert x.a == w.d.c.b.a
assert x.a ==
