import weakref
# Test weakref.ref()
import _weakref

class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o
assert isinstance(r, weakref.ReferenceType)
assert r.__class__ is weakref.ref

class D(object):
    def __init__(self, arg):
        self.arg = arg

o = D(42)
r = weakref.ref(o, lambda arg: arg.arg)
assert r() is o
assert isinstance(r, weakref.ReferenceType)
assert r.__class__ is weakref.ref

# Test weakref.proxy()
import weakref
# Test weakref.proxy()
import _weakref

class C(object):
    pass

o = C()
p = weakref.proxy(o)
assert p is o
assert isinstance(p, weakref.ProxyType)
assert p.__class__ is weakref.ProxyType
assert p.__weakref__ is not None

