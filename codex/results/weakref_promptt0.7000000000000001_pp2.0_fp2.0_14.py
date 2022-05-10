import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
assert r() is o
assert weakref.getweakrefcount(o) == 1
assert weakref.getweakrefs(o) == [r]

# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
d[o] = 1
assert d[o] == 1
del o
assert len(d) == 0

# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
d["1"] = o
assert d["1"] is o
del o
assert len(d) == 0

# Test weakref.WeakSet
s = weakref.WeakSet()
s.add(o)
assert o in s
del o
assert len(s) == 0

# Test weakref.finalize
sentinel = object()
def callback(*args):
    global sentinel
    sentinel = args

o = C()
f = weakref.finalize(o, callback, "hello")
assert f.alive
