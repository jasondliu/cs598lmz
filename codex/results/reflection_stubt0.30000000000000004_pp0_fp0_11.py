fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the iterator is closed when the code object is deallocated.
# This is a regression test for issue #16056.
import gc
import weakref

# Create a code object with a generator iterator.
def fn():
    yield 1

# Create a weak reference to the iterator.
it = iter(fn.__code__.co_consts)
it_ref = weakref.ref(it)

# Delete the code object.
del fn.__code__

# Collect the code object.
gc.collect()

# Check that the iterator is closed.
assert it_ref() is None
