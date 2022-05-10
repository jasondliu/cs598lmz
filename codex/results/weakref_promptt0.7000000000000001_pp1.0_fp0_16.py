import weakref
# Test weakref.ref
#
# The first reference to an object must be strong, so we store a strong reference
# in a list.
#
# Note that this test is deliberately not wrapped in a test case class.

class C(object):
    pass

def f():
    pass

l = [C(), C(), f, C(), 1, 'hello world', 1L, 3.14]

# Create some weak references
wref_l = [weakref.ref(x) for x in l]

# Delete all the strong references to the objects
del l

# Collect
import gc
gc.collect()

# Check that all the weak references are now dead
for i, x in enumerate(wref_l):
    y = x()
    if y is not None:
        raise AssertionError, "weak reference %d to %r is not dead" % (i, y)

# Check that a weak reference to a function can be called
wf = weakref.ref(f)
assert wf() is f
assert wf()() is None

# Check that a weak reference
