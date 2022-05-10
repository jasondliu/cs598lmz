import weakref
# Test weakref.ref

class C(object):
    pass

c = C()
ref = weakref.ref(c)
c2 = ref()
assert not (ref is None or c2 is None)

del c, c2
# Test weakref.proxy

class C(object):
    pass

c = C()
p = weakref.proxy(c)
assert isinstance(p, weakref.ProxyType)
assert p.__class__ is C
assert p.__dict__ is c.__dict__
assert bool(p)
assert p.__bool__()

c2 = C()
p2 = weakref.proxy(c2)
assert p2.__dict__ is c2.__dict__
assert p.__dict__ is c.__dict__
assert bool(p2)
assert p2.__bool__()

del c, c2, p, p2

# Test weakref.getweakrefcount

class C(object):
    pass

c = C()
p = weakref.proxy(c)
assert weakref.getweakrefcount
