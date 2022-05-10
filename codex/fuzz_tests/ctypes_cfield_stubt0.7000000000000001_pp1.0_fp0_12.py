import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    pass

A._fields_ = [('a', ctypes.c_int)]

class B(A):
    _fields_ = [('b', ctypes.c_int)]

class C(B):
    _fields_ = [('c', ctypes.c_int)]

class D(C):
    _fields_ = [('d', ctypes.c_int)]

class E(D):
    _fields_ = [('e', ctypes.c_int)]

for cls in (A, B, C, D, E):
    print cls, ':', len(cls._fields_), 'field(s)'

print len(E._fields_), 'field(s) for E'
print E._fields_[2][0]

res = []
for cls in (D, C, B, A):
    res.extend(cls._fields_)
print 'res:', res
</code>
output:
<code>A : 1 field(s)
B
