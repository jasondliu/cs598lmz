import weakref
# Test weakref.ref
def f():
    return 42

x = f()
assert x == 42
r = weakref.ref(f)
assert r()() == 42
del f
assert r() is None
# Test weakref.proxy
o = object()
p = weakref.proxy(o)
assert p is o
del o
try:
    p is o
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")
# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
o = object()
d[1] = o
assert d[1] is o
del o
assert len(d) == 0
# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
o = object()
d[o] = 42
assert d[o] == 42
del o
assert len(d) == 0
# Test weakref.WeakSet
s = weakref.WeakSet()
o = object()
s.add(o)
assert o in s
del o
assert len(s) == 0
# Test
