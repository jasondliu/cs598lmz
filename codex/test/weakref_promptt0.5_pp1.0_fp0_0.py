import weakref
# Test weakref.ref()

class Foo(object):
    pass

a = Foo()
r = weakref.ref(a)
assert r() is a

a = Foo()
r = weakref.ref(a)
assert r() is a

# Test weakref.proxy()

a = Foo()
p = weakref.proxy(a)
assert p is a

a = Foo()
p = weakref.proxy(a)
assert p is a

# Test weakref.getweakrefcount()

assert weakref.getweakrefcount(a) == 1

# Test weakref.getweakrefs()

l = weakref.getweakrefs(a)
assert len(l) == 1
assert l[0]() is a

# Test weakref.ref() with a callable

def foo():
    pass

a = Foo()
r = weakref.ref(foo, a)
assert r() is a

a = Foo()
r = weakref.ref(foo, a)
assert r() is a

# Test weakref.proxy() with
