import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Test:
    pass

for i in range(100):
    Test()

gc.set_threshold(500, 10, 10)
# Force collection
gc.collect()
import gc, weakref

class C:
    pass

c = C()
wr = weakref.ref(c)
print(wr)

del c
gc.collect()
print(wr)
gc.get_threshold()
gc.set_threshold(700, 10, 10)
gc.get_threshold()
import gc
gc.set_debug(gc.DEBUG_STATS)
gc.collect()
gc.set_debug(gc.DEBUG_LEAK)
gc.collect()
import gc
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.collect()
import gc
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()
import gc
gc.is_tracked(object())
gc.set_debug(gc.DEBUG_STATS)
gc.collect()
 
 
import
