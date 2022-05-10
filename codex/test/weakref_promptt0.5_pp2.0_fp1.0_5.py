import weakref
# Test weakref.ref
import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
del o
assert r() is None
assert r() is None

# Test weakref.ref with callbacks
import weakref

called = []

def callback(r):
    called.append(r)

class C:
    pass

o = C()
r = weakref.ref(o, callback)
assert r() is o
del o
assert r() is None
assert called == [r]

# Test weakref.ref with callbacks, and a second reference
import weakref

called = []

def callback(r):
    called.append(r)

class C:
    pass

o = C()
r = weakref.ref(o, callback)
s = weakref.ref(o)
assert r() is o
del o
assert r() is None
assert s() is None
assert called == [r]

# Test weakref.ref with callbacks, and a cycle
import weakref
