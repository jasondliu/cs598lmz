import weakref
# Test weakref.ref

class A:
    pass

a = A()
r = weakref.ref(a)
assert r() is a
assert r() is not None
del a
assert r() is None

# Test weakref.proxy

class B:
    pass

b = B()
p = weakref.proxy(b)
assert p is b
assert p is not None
del b
try:
    p.attr
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")

# Test weakref.getweakrefcount

assert weakref.getweakrefcount(a) == 0
assert weakref.getweakrefcount(b) == 0

# Test weakref.getweakrefs

assert weakref.getweakrefs(a) == []
assert weakref.getweakrefs(b) == []

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
d[a] = 1
assert d[a] == 1
del a
assert d == {}

# Test weakref.WeakValue
