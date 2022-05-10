import ctypes
# Test ctypes.CField
class C(Structure):
    _fields_ = [('i', c_int)]

class D(C):
    _fields_ = [('j', c_int)]

assert type(D.j) == CFieldType
assert D.j.offset == ctypes.sizeof(c_int)
assert D.j.ctype is c_int

class E(D):
    _fields_ = [('k', c_int)]

assert E.k.offset == D.j.offset + ctypes.sizeof(c_int)
assert E.k.ctype is c_int

# Test CFieldType.from_field
a = CFieldType.from_field('a', 'i', offset=0, ctype=c_int)
assert a.offset == 0
assert a.ctype is c_int

b = CFieldType.from_field('b', 'j', offset=ctypes.sizeof(c_int), ctype=c_int, use_dealloc=True)
assert b.offset == ctypes.sizeof(c_int
