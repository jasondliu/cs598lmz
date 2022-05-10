import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
assert r() is o
o2 = r()
assert o2 is o
o = None
assert r() is None
assert r() is None

# Test weakref.WeakKeyDictionary
import weakref
d = weakref.WeakKeyDictionary()
o1 = C()
o2 = C()
d[o1] = 1
d[o2] = 2
assert d[o1] == 1
assert d[o2] == 2
del o2
assert d[o1] == 1
assert list(d) == [o1]
del o1
assert len(d) == 0

# Test weakref.WeakValueDictionary
import weakref
d = weakref.WeakValueDictionary()
o1 = C()
o2 = C()
d[1] = o1
d[2] = o2
assert d[1] is o1
assert d[2] is o2
del o2
assert d[1] is o1
assert list(d)
