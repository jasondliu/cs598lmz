import weakref
# Test weakref.ref
import weakref
class Foo(object):
    pass
a = Foo()
r = weakref.ref(a)
print r
print type(r)
print r().__class__
print 

import weakref
e = Foo()
r = weakref.ref(e)
print r
print type(r)

e = 10
print r
print type(r)
print 

e = []

# Test finaliser
class A(object):
    pass
def callNext(next, a):
    print a.__class__
    next()
class B(object):
    def __init__(self):
        self.a = A()
        weakref.finalize(self, callNext, self.a)
b = B()
print

# Test __del__ is only called once
class C(object):
    def __del__(self):
        pass
c = C()
r = weakref.ref(c)
b = r()
print type(b)
b = r()
print type(b)
r = r()
print r
