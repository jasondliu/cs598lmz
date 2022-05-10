import weakref
# Test weakref.ref

class Foo:
    pass

a = Foo()
r = weakref.ref(a)
assert r() is a
del a
assert r() is None

# Test weakref.proxy

a = Foo()
p = weakref.proxy(a)
assert p is a
del a
try:
    p.attr
except ReferenceError:
    pass
else:
    assert False, "expected ReferenceError"

# Test weakref.getweakrefcount

a = Foo()
assert weakref.getweakrefcount(a) == 0
r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1
w = weakref.proxy(a)
assert weakref.getweakrefcount(a) == 2
del r
assert weakref.getweakrefcount(a) == 1
del w
assert weakref.getweakrefcount(a) == 0

# Test weakref.getweakrefs

a = Foo()
assert weakref.getweakrefs(a) == []
r = weakref.ref(a)

