import weakref
# Test weakref.ref

class Foo:
    pass

foo = Foo()
f = weakref.ref(foo)

foo.x = 10
assert f().x == 10

del foo
assert f() is None
