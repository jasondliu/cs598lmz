import weakref
# Test weakref.ref
import weakref

class C(object):
    pass

o = C()
r = weakref.ref(o)
assert r() is o
assert r is not o

class D(object):
    pass

o = D()
r = weakref.ref(o)
assert r() is o
assert r is not o

class E(object):
    pass

o = E()
r = weakref.ref(o)
assert r() is o
assert r is not o

# Test weakref.proxy
import weakref

class C(object):
    pass

o = C()
p = weakref.proxy(o)
assert p is o

class D(object):
    pass

o = D()
p = weakref.proxy(o)
assert p is o

class E(object):
    pass

o = E()
p = weakref.proxy(o)
assert p is o

# Test weakref.finalize
import weakref

class C(object):
    pass

o = C()
f =
