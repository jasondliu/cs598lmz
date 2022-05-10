import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# gc.collect() returns the number of objects collected and
# uncollectable.
#
# If the number of uncollectable objects is non-zero, a
# GarbageError is raised.
#
# This test checks that gc.collect() does not crash, and that
# the number of uncollectable objects is zero.
#
# This test is not exhaustive.  It only checks a few cases.
#
# See also test_weakref.py.

import gc

# Check that gc.collect() doesn't crash.
gc.collect()

# Check that gc.collect() doesn't crash with a callback.
def callback(x):
    pass
gc.collect(callback)

# Check that gc.collect() doesn't crash with a callback that
# raises an exception.
def badcallback(x):
    raise ValueError
try:
    gc.collect(badcallback)
except ValueError:
    pass

# Check that gc.collect() doesn't crash with a callback that
# raises an exception in a try block.
def badcallback
