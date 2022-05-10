import weakref
# Test weakref.ref(x) == weakref.ref(x)

class Foo:
    pass

foo = Foo()
wr1 = weakref.ref(foo)
wr2 = weakref.ref(foo)
assert wr1 is wr2

# Test weakref.ref(x) == weakref.ref(y)

class Foo:
    pass

foo = Foo()
bar = Foo()
wr1 = weakref.ref(foo)
wr2 = weakref.ref(bar)
assert wr1 != wr2

# Test weakref.ref(x) == x

class Foo:
    pass

foo = Foo()
wr1 = weakref.ref(foo)
assert wr1 == foo

# Test x == weakref.ref(x)

class Foo:
    pass

foo = Foo()
wr1 = weakref.ref(foo)
assert foo == wr1

# Test weakref.ref(x) != x

class Foo:
    pass

foo = Foo()
wr1 = weakref.ref(foo)
assert wr1 != foo


