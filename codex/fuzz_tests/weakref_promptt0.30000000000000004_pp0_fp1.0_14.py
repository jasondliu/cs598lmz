import weakref
# Test weakref.ref() and weakref.proxy()

# Test weakref.ref()

class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o

o2 = C()
r2 = weakref.ref(o2)
assert r2() is o2

o = o2 = None
assert r() is None
assert r2() is None

# Test weakref.proxy()

class D(object):
    pass

o = D()
p = weakref.proxy(o)
assert p.__class__ is weakref.ProxyType
assert p is o

o2 = D()
p2 = weakref.proxy(o2)
assert p2.__class__ is weakref.ProxyType
assert p2 is o2

o = o2 = None
try:
    p.x
except ReferenceError:
    pass
else:
    raise Exception("Dereferencing dead proxy should have raised ReferenceError")

try:
    p2.x
except ReferenceError:
    pass
else:
