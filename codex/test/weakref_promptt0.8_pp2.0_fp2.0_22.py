import weakref
# Test weakref.ref(lambda: 1) -- this used to crash, and was reported
# in comp.lang.python on 2006-04-30.
class X(object):
    pass

def foo(x):
    return x + 1

x = X()
x.f = foo
# The lambda's closure should contain a strong reference to x.
# This used to be a bug with __slots__ (for x and X).
y = weakref.ref(lambda: x.f(x))
