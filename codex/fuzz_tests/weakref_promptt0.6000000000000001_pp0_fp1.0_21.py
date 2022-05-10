import weakref
# Test weakref.ref()
w = weakref.ref(3)
assert w() == 3
assert w() is 3

a = weakref.ref(1)
b = weakref.ref(2)
c = weakref.ref(1)
assert a is c
assert a is not b
assert a() is 1
assert b() is 2
assert c() is 1

# Test weakref.WeakKeyDictionary()
a = weakref.WeakKeyDictionary()
a[1] = 2
assert len(a) == 1
assert 1 in a
assert 2 in a
assert 2 in a.values()
assert 2 in a.itervalues()
assert 1 in a.keys()
assert 1 in a.iterkeys()
assert (1, 2) in a.items()
assert (1, 2) in a.iteritems()

# Test weakref.WeakValueDictionary()
a = weakref.WeakValueDictionary()
a[1] = 2
assert len(a) == 1
assert 1 in a
assert 2 in a
assert 2 in a.values()
assert 2 in a.it
