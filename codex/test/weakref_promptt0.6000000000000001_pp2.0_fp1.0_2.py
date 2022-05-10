import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
del o
assert r() is None
# Test weakref.WeakKeyDictionary()

class C:
    pass

d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
assert o in d
del o
assert len(d) == 0
# Test weakref.WeakValueDictionary()

class C:
    pass

d = weakref.WeakValueDictionary()
o = C()
d[1] = o
assert 1 in d
del o
assert len(d) == 0
# Test weakref.WeakSet()

class C:
    pass

s = weakref.WeakSet()
o = C()
s.add(o)
assert o in s
del o
assert len(s) == 0
# Test weakref.finalize()

class C:
    pass

o = C()
l = []

