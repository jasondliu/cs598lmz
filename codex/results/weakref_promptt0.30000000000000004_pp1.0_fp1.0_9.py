import weakref
# Test weakref.ref(x) == weakref.ref(x)

class Foo:
    pass

a = Foo()
b = Foo()

assert weakref.ref(a) == weakref.ref(a)
assert weakref.ref(a) != weakref.ref(b)
assert weakref.ref(b) != weakref.ref(a)
assert weakref.ref(b) == weakref.ref(b)

# Test weakref.ref(x) == x

assert weakref.ref(a) == a
assert weakref.ref(b) == b

# Test x == weakref.ref(x)

assert a == weakref.ref(a)
assert b == weakref.ref(b)

# Test weakref.ref(x) != x

assert weakref.ref(a) != a
assert weakref.ref(b) != b

# Test x != weakref.ref(x)

assert a != weakref.ref(a)
assert b != weakref.ref(b)

# Test weakref.ref(x) is
