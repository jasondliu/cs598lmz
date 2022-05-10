import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f

del f
assert r() is None

# Test weakref.proxy()

class Foo:
    pass

f = Foo()
p = weakref.proxy(f)
assert p is f

del f
try:
    p.attr
except ReferenceError:
    pass
else:
    assert False, "expected ReferenceError"

# Test weakref.getweakrefcount()

class Foo:
    pass

f = Foo()
assert weakref.getweakrefcount(f) == 0

r = weakref.ref(f)
assert weakref.getweakrefcount(f) == 1

p = weakref.proxy(f)
assert weakref.getweakrefcount(f) == 2

# Test weakref.getweakrefs()

class Foo:
    pass

f = Foo()
assert weakref.getweakrefs(f) == []

r = weakref.ref(f)
