import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() by creating a reference cycle
# and making sure that it gets broken when the
# cycle is collected.
#
# This is a variant of test_gc.py:test_collect2

class A:
    pass

class B:
    pass

a = A()
b = B()

a.x = b
b.x = a

# Now create a reference cycle with a weakref
a.y = weakref.ref(b)
b.y = weakref.ref(a)

# Now make sure that the reference cycle gets broken
# when we collect

del a, b

import gc
gc.collect()

# Check that we've collected the cycle

assert gc.collect() == 0

# Check that we've collected the cycle
# by running the garbage collector
# in debug mode

gc.collect()

# Check that we've collected the cycle
# by running the garbage collector
# in debug mode

gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
gc.collect()
gc.
