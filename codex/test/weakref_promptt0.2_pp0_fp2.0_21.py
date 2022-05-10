import weakref
# Test weakref.ref
class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f
del f
assert r() is None
# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
f = Foo()
d[f] = 1
assert d[f] == 1
del f
assert len(d) == 0
# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
f = Foo()
d[1] = f
assert d[1] is f
del f
assert len(d) == 0
# Test weakref.WeakSet
s = weakref.WeakSet()
f = Foo()
s.add(f)
assert f in s
del f
assert len(s) == 0
# Test weakref.finalize
f = Foo()
r = weakref.finalize(f, lambda: None)
assert r.alive
del f
assert not r.alive
# Test weakref.proxy
f = Foo()
p = weakref.proxy(f)
