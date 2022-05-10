import weakref
# Test weakref.ref, weakref.proxie

# Create an object with a __weakref__, and use weakref.proxy() to obtain
# a proxy to it.
class Foo:
    pass

foo1 = Foo()
def f():
    print "foo1 was deleted"

f1 = weakref.ref(foo1, f)
f2 = weakref.proxy(foo1)

print f1(), f2

# Delete the original object:
del foo1

# Now accessing f1() or f2 should call f()
print f1(), f2
print f1() is None

try:
    print f2.attr
except ReferenceError:
    pass
else:
    print "Expected ReferenceError"


# The same thing, but this time, __weakref__ is a list.
class Foo:
    pass

foo1 = Foo()
foo1.__weakref__ = []
def f():
    print "foo1 was deleted"

f1 = weakref.ref(foo1, f)
f2 = weakref.proxy(foo1)


