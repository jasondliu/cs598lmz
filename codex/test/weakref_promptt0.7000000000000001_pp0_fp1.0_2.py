import weakref
# Test weakref.ref()
def f():
    pass
a = f
del f
r = weakref.ref(a)
assert r() is a

a = None
gc.collect()       # forcing gc is needed to exercise the bug
assert r() is None

# Test weakref.getweakrefcount()
a = []
assert weakref.getweakrefcount(a) == 0
r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1

# Test weakref.getweakrefs()
l = weakref.getweakrefs(a)
assert r in l and len(l) == 1

# Test weakref.proxy()
b = weakref.proxy(a)
assert b == a
assert weakref.getweakrefcount(a) == 2

# Test the attribute access of weakref.proxy()
a.append(1)
b.append(2)
assert a == [1, 2]
assert a[0] == 1
assert b[1] == 2

# Test the deleter of weakref.proxy()
del b
