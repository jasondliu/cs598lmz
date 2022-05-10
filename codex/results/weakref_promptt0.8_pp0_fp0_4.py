import weakref
# Test weakref.ref() and weakref.KeyedRef() with
# weakref.WeakKeyDictionary and weakref.WeakValueDictionary.
# Also test __repr__
a = []
d = weakref.WeakKeyDictionary()
d[a] = 1
r = weakref.ref(a)
r2 = weakref.KeyedRef(r, a)
assert r() is a
assert r2() is 1
assert repr(r) == '<weakref at %x; dead>' % id(r)
assert str(r) == '<weakref at %x; dead>' % id(r)
del a
assert r() is None
assert r2() is None
assert repr(r) == '<weakref at %x; dead>' % id(r)
assert str(r) == '<weakref at %x; dead>' % id(r)

a = []
d = weakref.WeakValueDictionary()
d[1] = a
r = weakref.ref(a)
r2 = weakref.KeyedRef(r, 1)
assert r
