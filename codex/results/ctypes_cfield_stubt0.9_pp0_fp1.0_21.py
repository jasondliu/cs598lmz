import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('b', ctypes.c_char), ('p', ctypes.POINTER(S))]

class B(ctypes.Structure):
    _fields_ = [('b', ctypes.c_char), ('p', ctypes.POINTER(S))]

t = type(B.p)
assert issubclass(t, ctypes.CField)
print(isinstance(B.p, ctypes.CField))
a = A()
assert type(a.b) is ctypes.c_char
s = S()
pointer_to_s = ctypes.pointer(s)
# Python has more info then ctypes.Field, so you can figure out if
# you are casting to the right type.
a.p = pointer_to_s
b = B()
b.b = 'b'
b.p = a.p
# Try a write woth b.p[0].x = 42
b.p[0].x = 42
assert b.p[0].x == 42
