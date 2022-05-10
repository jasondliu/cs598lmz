import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when the weakref callback is invoked.
# This is a regression test for SF bug #836134:
# http://sourceforge.net/tracker/index.php?func=detail&aid=836134&group_id=5470&atid=105470

# The important thing is that when the callback is invoked,
# the object is still reachable: the weakref should not be
# considered dead.

# If this test fails, the "gc.garbage" list will be non-empty.

from sys import getrefcount

class X(object):
    pass

x = X()
w = weakref.ref(x, lambda w: x)

# x is not the only reference to X
assert getrefcount(x) > 1
# w is not the only reference to the weakref
assert getrefcount(w) > 1

x = "abc"

gc.collect()

# x is gone and the weakref is dead
assert x is "abc"
assert w() is None
