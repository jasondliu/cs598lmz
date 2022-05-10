import weakref
# Test weakref.ref and weakref.proxy.

# Weak references to objects
class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o
assert type(r) is weakref.ReferenceType

o2 = C()
r2 = weakref.ref(o2)
assert r2() is o2
assert r2 is not r

# Test weakref.proxy
p = weakref.proxy(o)
assert p.__class__ is weakref.ProxyType
assert type(p) is C
assert p is o
assert p.foo == o.foo == 42

p2 = weakref.proxy(o2)
assert p2.__class__ is weakref.ProxyType
assert type(p2) is C
assert p2 is o2
assert p2.foo == o2.foo == 42

class C(object):
    def __init__(self, x):
        self.x = x
    def foo(self, y):
        return self.x + y

o = C(40)
p = weak
