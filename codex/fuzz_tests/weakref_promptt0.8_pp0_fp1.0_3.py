import weakref
# Test weakref.ref() for ints, floats, and longs.

l = 1L
d = 2.0

for x in 2, 2.0:
    assert isinstance(weakref.ref(x), weakref.ReferenceType)

for x in 2L, d:
    assert isinstance(weakref.ref(x), weakref.ReferenceType)

# Issue #10206: Test that weakrefs to builtin types call __del__ on its referents,
# and that __del__ is called before the self argument is cleared.

class TestClass:
    called = False

    def __del__(self):
        TestClass.called = True

t = TestClass()

# Test that __del__ is called before the self argument is cleared,
# by checking whether we can still read current class' attribute.

r = weakref.ref(t)
r()
del t
del r

assert TestClass.called
