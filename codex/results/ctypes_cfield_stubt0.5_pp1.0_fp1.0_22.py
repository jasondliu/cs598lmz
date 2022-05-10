import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(D):
    _fields_ = [('z', ctypes.c_int)]

# Test the 'offset' attribute
assert S.x.offset == 0
assert C.x.offset == 0
assert D.x.offset == 0
assert D.y.offset == ctypes.sizeof(ctypes.c_int)
assert E.x.offset == 0
assert E.y.offset == ctypes.sizeof(ctypes.c_int)
assert E.z.offset == ctypes.sizeof(ctypes.c_int) * 2

# Test the 'from_address()' method
s = S()
c = C()
d = D()
e = E()

assert S.x.from_address(ctypes.addressof(s)).value == 0
assert C.x.from_address(ctypes.add
