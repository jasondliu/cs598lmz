import weakref
# Test weakref.ref()
import _weakref

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
assert r() is o

r = weakref.ref(o, lambda o: None)
assert r() is o
assert r() is o

r = weakref.ref(o, lambda o: None)
assert r() is o
assert r() is o

r = weakref.ref(o, lambda o: None)
assert r() is o
assert r() is o

r = weakref.ref(o, lambda o: None)
assert r() is o
assert r() is o

r = weakref.ref(o, lambda o: None)
assert r() is o
assert r() is o

r = weakref.ref(o, lambda o: None)
assert r() is o
assert r() is o

r = weakref.ref(o, lambda o: None)
assert r() is o
assert r() is o

r = weakref.ref(o, lambda o: None)

