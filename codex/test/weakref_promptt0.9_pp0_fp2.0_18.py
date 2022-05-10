import weakref
# Test weakref.ref with functions

import weakref

def foo():
    pass

r = weakref.ref(foo)
assert r() is foo

del foo
assert r() is None

# Create a new function to test that the former one
# isn't revived.

def foo():
    pass

assert r() is None
# Test weakref.ref with exception instances

import weakref, exceptions

e = exceptions.Exception()
r = weakref.ref(e)
assert r() is e

del e
assert r() is None

# Create a new exception to test that the former
# one isn't revived.

e = exceptions.Exception()
assert r() is None
# Test weakref.ref with methods

import weakref

class A:
    def foo(self):
        pass

a = A()
m = a.foo
r = weakref.ref(m)
assert r() is m

del a
# The method must still be there
assert isinstance(r(), weakref.ref)

del m
# The method must be gone now
