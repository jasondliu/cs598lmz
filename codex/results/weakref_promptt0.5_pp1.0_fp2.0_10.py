import weakref
# Test weakref.ref() for objects that are not subclasses of object.

class C:
    pass

c = C()
r = weakref.ref(c)
assert r() is c

c = None
assert r() is None
