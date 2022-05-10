import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    pass

C._fields_ = [
    ('a', ctypes.c_char),
    ('b', ctypes.c_char),
    ('c', ctypes.CField)
]

class D(ctypes.Structure):
    pass

D._fields_ = [
    ('a', ctypes.c_char),
    ('b', ctypes.CField)
]

class E(ctypes.Structure):
    pass

E._fields_ = [
    ('a', ctypes.c_char),
    ('b', ctypes.c_char),
    ('c', ctypes.c_char),
    ('d', ctypes.CField)
]
print E
print D
print C

print dir(E)
print dir(D)
print dir(C)

print E.a
print E.b
print E.c
print E.d

print E.__dict__
print D.__dict__
print C.__dict__

print E.in_dll
