import weakref
# Test weakref.ref()

# Test that weakref.ref() returns a weak reference to its argument.

import weakref

class A(object):

    def __init__(self, x):
        self.x = x

def ref(x):
    return weakref.ref(x)

def deref(r):
    return r()

a = A(42)
ra = ref(a)
b = deref(ra)
assert b is a
assert b.x == 42

# Test that weakref.ref() raises TypeError when the argument is not weakly
# referencable.

try:
    r = ref(1)
except TypeError:
    pass
else:
    assert False, "expected TypeError"
