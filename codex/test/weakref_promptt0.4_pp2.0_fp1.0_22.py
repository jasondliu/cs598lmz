import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

o2 = C()
r2 = weakref.ref(o2, lambda x: print('dead'))
assert r2() is o2

o = None
assert r() is None
assert r2() is None

# Test weakref.WeakKeyDictionary

class C:
    pass

d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
assert len(d) == 1
assert d[o] == 1

o2 = C()
d[o2] = 2
assert len(d) == 2
assert d[o2] == 2

del o
assert len(d) == 1
assert d[o2] == 2

del o2
assert len(d) == 0

# Test weakref.WeakValueDictionary

class C:
    pass

d = weakref.WeakValueDictionary()
o = C()
d['a'] = o
assert len
