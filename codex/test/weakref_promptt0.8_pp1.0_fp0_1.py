import weakref
# Test weakref.ref(foo) returns the same value each time
# instead of a new weakref.
class C(object):
    pass
c = C()
foo = weakref.ref(c)
assert foo() is c
assert isinstance(foo, weakref.ref)
for i in range(10):
    assert foo() is c

# C is now unreachable
del c

assert foo() is None

# Issue 1429
# Weakrefs of weakrefs

class A(object):
    pass

# Make sure that A is not collected
a = A()

x = weakref.ref(a)
y = weakref.ref(x)
z = weakref.ref(y)

del a, x, y

# Before, this would blow up with a segfault
assert z() is None
