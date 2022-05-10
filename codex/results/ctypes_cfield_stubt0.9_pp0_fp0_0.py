import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

s = S()

s.x = 1

assert int(s.x) == 1
assert repr(s.x) == repr(1)
assert float(s.x) == 1.0
assert float(S(x=1).x) == 1.0

assert s.x < 2
assert s.x >= 0
assert s.x <= 1
assert s.x != 2
assert s.x == 1

assert ctypes.CField(1) < 2
assert ctypes.CField(1) <= 1
assert ctypes.CField(1) != 2
assert ctypes.CField(1) == 1

assert s.x + 0.1 == 1.1

# Test case for initializing fields with non-integers

class X(ctypes.Structure):
    _fields_ = [('f', ctypes.c_float)]

x = X(f=0.5)

assert x.f == 0.5

class Y(X):
    _fields_ = X._fields_ + [('f', ctypes.c_
