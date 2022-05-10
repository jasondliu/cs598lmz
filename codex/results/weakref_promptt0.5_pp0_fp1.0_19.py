import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    pass

a = Foo()
r = weakref.ref(a)
assert r() is a

p = weakref.proxy(a)
assert p is a

a = None
assert r() is None

try:
    p.attr
except ReferenceError:
    pass
else:
    raise Exception("should have raised ReferenceError")

# Test weakref.getweakrefcount()

assert weakref.getweakrefcount(Foo()) == 0

a = Foo()
assert weakref.getweakrefcount(a) == 0

r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1

p = weakref.proxy(a)
assert weakref.getweakrefcount(a) == 2

# Test weakref.getweakrefs()

assert weakref.getweakrefs(Foo()) == []

a = Foo()
assert weakref.getweakrefs(a) == []

r = weakref.ref(a)
assert weak
