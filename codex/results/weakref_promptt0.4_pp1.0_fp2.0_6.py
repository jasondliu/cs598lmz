import weakref
# Test weakref.ref()
class C(object):
    pass

c = C()
r = weakref.ref(c)
assert r() is c

r = weakref.ref(c, lambda o: None)
assert r() is c

r = weakref.ref(c, lambda o: None)
assert r() is c

r = weakref.ref(c, lambda o: None)
assert r() is c

r = weakref.ref(c, lambda o: None)
assert r() is c

r = weakref.ref(c, lambda o: None)
assert r() is c

r = weakref.ref(c, lambda o: None)
assert r() is c

r = weakref.ref(c, lambda o: None)
assert r() is c

r = weakref.ref(c, lambda o: None)
assert r() is c

r = weakref.ref(c, lambda o: None)
assert r() is c

r = weakref.ref(c, lambda o: None)
assert r() is c

r
