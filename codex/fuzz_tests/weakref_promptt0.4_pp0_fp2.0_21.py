import weakref
# Test weakref.ref()
def f():
    return 42

x = f()
assert x == 42
r = weakref.ref(x)
assert r() == 42
del x
assert r() == 42

# Test weakref.proxy()
x = f()
p = weakref.proxy(x)
assert p == 42
del x
assert p == 42

# Test weakref.getweakrefcount()
x = f()
assert weakref.getweakrefcount(x) == 0
r = weakref.ref(x)
assert weakref.getweakrefcount(x) == 1
p = weakref.proxy(x)
assert weakref.getweakrefcount(x) == 2

# Test weakref.getweakrefs()
x = f()
assert weakref.getweakrefs(x) == []
r = weakref.ref(x)
assert weakref.getweakrefs(x) == [r]
p = weakref.proxy(x)
assert weakref.getweakrefs(x) == [r, p]

# Test weakref.WeakKey
