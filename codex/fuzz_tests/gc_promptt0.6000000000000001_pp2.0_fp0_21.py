import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# gc.collect() should collect all unreachable objects, and
# return the number of unreachable objects collected and
# deallocated.

import sys
import gc

def check_everything_is_collectable():
    # Check that everything is collectable.
    l = gc.collect()
    if l != 0:
        raise TestFailed("gc.collect() found %d unreachable objects" % (l,))

class C:
    pass

def check_everything_is_collectable_except_C():
    # Check that everything is collectable.
    l = gc.collect()
    if l != 1:
        raise TestFailed("gc.collect() found %d unreachable objects" % (l,))

# Create a bunch of objects.

check_everything_is_collectable()

del x, y, z

a = C()
b = C()
c = C()
d = C()
e = C()
f = C()

check_everything_is_collectable()

# Create a cycle.

