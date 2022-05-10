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
try:
    p == 42
except ReferenceError:
    pass
else:
    assert False

# Test weakref.getweakrefcount()
x = f()
assert weakref.getweakrefcount(x) == 0
r = weakref.ref(x)
assert weakref.getweakrefcount(x) == 1
del r
assert weakref.getweakrefcount(x) == 0

# Test weakref.getweakrefs()
x = f()
assert weakref.getweakrefs(x) == []
r = weakref.ref(x)
assert weakref.getweakrefs(x) == [r]
del r
assert weakref.getweakrefs(x) == []

