import weakref
# Test weakref.ref()
def f():
    pass
r = weakref.ref(f)
assert r() is f
# Test weakref.proxy()
p = weakref.proxy(f)
assert p is f

# Test weakref.WeakKeyDictionary()
d = weakref.WeakKeyDictionary()
d[f] = 1
assert d[f] == 1
del f
assert len(d) == 0

# Test weakref.WeakValueDictionary()
d = weakref.WeakValueDictionary()
d[1] = f
assert d[1] is f
del f
assert len(d) == 0

# Test weakref.WeakSet()
s = weakref.WeakSet()
s.add(f)
assert f in s
del f
assert len(s) == 0

# Test weakref.finalize()
l = []
def callback(x):
    l.append(x)
del l[:]
obj = object()
finalizer = weakref.finalize(obj, callback, obj)
assert finalizer.alive
del obj
gc.collect
