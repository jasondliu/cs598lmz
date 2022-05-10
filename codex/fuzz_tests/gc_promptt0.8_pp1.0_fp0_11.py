import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after an object is deleted from a set
# without invoking a __del__ method.

import gc
gc.set_debug(gc.DEBUG_LEAK)
# Allocate some garbage.
class C:
    def __del__(self):
        pass
for i in range(10):
    x = C()
    y = C()
    x.attr = y
    y.attr = x

del x, y
gc.collect()

print(gc.garbage)
gc.set_debug(0)
