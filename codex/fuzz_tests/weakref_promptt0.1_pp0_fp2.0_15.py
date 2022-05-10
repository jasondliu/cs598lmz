import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert r() is f

f = None
assert r() is None

# Test weakref.proxy()

f = Foo()
p = weakref.proxy(f)
assert p is f

f = None
try:
    p.attr
except ReferenceError:
    pass
else:
    raise Exception("should have raised ReferenceError")

# Test weakref.getweakrefcount()

f = Foo()
assert weakref.getweakrefcount(f) == 0

r = weakref.ref(f)
assert weakref.getweakrefcount(f) == 1

p = weakref.proxy(f)
assert weakref.getweakrefcount(f) == 2

# Test weakref.getweakrefs()

f = Foo()
assert weakref.getweakrefs(f) == [r, p]

# Test weakref.WeakKeyDictionary()

d = weakref.WeakKeyDictionary()
f = Foo()

