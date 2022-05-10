import weakref
# Test weakref.ref()
def f(): pass
r = weakref.ref(f)
assert r() is f

# Test weakref.proxy()
p = weakref.proxy(f)
assert p is f

# Test weakref.getweakrefcount()
assert weakref.getweakrefcount(f) == 2

# Test weakref.getweakrefs()
assert f in weakref.getweakrefs(f)
assert p in weakref.getweakrefs(f)

# Test weakref.WeakKeyDictionary()
class C: pass
d = weakref.WeakKeyDictionary()
c1 = C()
c2 = C()
d[c1] = 1
d[c2] = 2
assert len(d) == 2
del c1
assert len(d) == 1
del c2
assert len(d) == 0

# Test weakref.WeakValueDictionary()
d = weakref.WeakValueDictionary()
c1 = C()
c2 = C()
d[1] = c1
d[2] = c2
