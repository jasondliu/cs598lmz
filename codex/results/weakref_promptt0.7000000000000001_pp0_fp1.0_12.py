import weakref
# Test weakref.ref.__call__()
# This is a test of weakref.ref.__call__()
import weakref

class Foo(object):
    def __call__(self, *args, **kwargs):
        return (args, kwargs)

f = Foo()
r = weakref.ref(f)
assert r() == ((), {})
assert r(1) == ((1,), {})
assert r(1, 2) == ((1, 2), {})
assert r(1, 2, 3) == ((1, 2, 3), {})
assert r(1, 2, 3, 4) == ((1, 2, 3, 4), {})
assert r(1, 2, 3, 4, 5) == ((1, 2, 3, 4, 5), {})
assert r(1, 2, 3, 4, 5, 6) == ((1, 2, 3, 4, 5, 6), {})
assert r(1, 2, 3, 4, 5, 6, 7) == ((1, 2, 3, 4, 5, 6, 7), {})
assert r
