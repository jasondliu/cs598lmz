import weakref
# Test weakref.ref()

class Foo:
    pass

foo = Foo()
r = weakref.ref(foo)
assert r() is foo

# Test weakref.proxy()

foo = Foo()
p = weakref.proxy(foo)
assert p is foo

# Test weakref.getweakrefcount()

foo = Foo()
r = weakref.ref(foo)
assert weakref.getweakrefcount(foo) == 1

# Test weakref.getweakrefs()

foo = Foo()
r = weakref.ref(foo)
assert weakref.getweakrefs(foo) == [r]

# Test weakref.WeakKeyDictionary()

d = weakref.WeakKeyDictionary()
foo = Foo()
d[foo] = 42
assert d[foo] == 42
del foo
assert d == {}

# Test weakref.WeakValueDictionary()

d = weakref.WeakValueDictionary()
foo = Foo()
d[42] = foo
assert d[42] is foo
del foo
assert d == {}

# Test
