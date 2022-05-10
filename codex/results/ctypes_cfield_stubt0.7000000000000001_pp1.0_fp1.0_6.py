import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
class A:
    pass

def descr_get(self, obj, objtype=None):
    print self, obj
    return 'get'

def descr_set(self, obj, value):
    print self, obj
    print value

A.x = ctypes.CField()
A.x.__get__ = descr_get
A.x.__set__ = descr_set

a = A()
print a.x
a.x = 'xxx'

#print S.x.__get__(S())

class A:
    var = 1

class B(A):
    pass

class D(A):
    var = 2

class C(B):
    pass

class E(C):
    pass

class F(D):
    pass

class G(E, F):
    pass

print G.var
print G.__mro__
print G.__bases__
