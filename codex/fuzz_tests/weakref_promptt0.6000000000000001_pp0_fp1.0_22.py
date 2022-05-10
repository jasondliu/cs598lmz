import weakref
# Test weakref.ref(x) is x and weakref.ref(weakref.ref(x)) is weakref.ref(x).
# Also test that the original weakref.ref() function is still accessible.
# This test will fail if weakref.ref has been replaced by a class.
r = weakref.ref(r)
r(r) is r
# Test that weakref.ref(x) returns the same result as weakref.ref(x, f),
# where f is an arbitrary callable.
r(r) is r(r, lambda : None)
