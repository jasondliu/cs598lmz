import weakref
# Test weakref.ref(1)
r = weakref.ref(1)
assert r() == 1
print(r.__class__.__name__)

#Test weakref.proxy(1)
p = weakref.proxy(1)
assert p == 1

#Test weakref.ref isinstance
assert isinstance(r, weakref.ReferenceType)
