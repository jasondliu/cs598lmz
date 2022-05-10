import weakref
# Test weakref.ref

class A:
    pass

a = A()
r = weakref.ref(a)
assert r() is a

# Test weakref.proxy

class B:
    def f(self):
        return 42

b = B()
p = weakref.proxy(b)
assert p.f() == 42

# Test weakref.getweakrefcount

assert weakref.getweakrefcount(b) == 0

# Test weakref.getweakrefs

assert weakref.getweakrefs(b) == []

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()

d[a] = 42
assert d[a] == 42
assert len(d) == 1

del a
assert len(d) == 0

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()

d[42] = a
assert d[42] is a
assert len(d) == 1

del a
assert len(d) == 0

# Test weakref.
