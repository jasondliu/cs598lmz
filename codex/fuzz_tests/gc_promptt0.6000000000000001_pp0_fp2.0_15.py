import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref.proxy objects.

import gc, weakref

class C:
    pass

c = C()
p = weakref.proxy(c)
del c

# p and the proxy object should be collectable
gc.collect()
#print gc.garbage
assert gc.garbage[0] is p
assert gc.garbage[1]() is None

# the proxy object should be in gc.garbage but not p
gc.collect()
#print gc.garbage
assert gc.garbage[0]() is None

# The proxy object should be gone now.
gc.collect()
#print gc.garbage
assert len(gc.garbage) == 0

# p should still be collectable
gc.collect()
#print gc.garbage
assert gc.garbage[0] is p
