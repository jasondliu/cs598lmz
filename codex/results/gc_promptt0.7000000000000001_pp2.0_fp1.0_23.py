import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
def f():
    a = A()
    a.b = A()
f()
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
# Test gc.collect()
class A:
    pass
def f():
    a = A()
    a.b = A()
f()
gc.collect()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(0)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.debug()
# Test gc.get_count()
gc.get_count()
gc.set_threshold(700)
gc.collect()
gc.get_count()
gc.set_threshold(1, 2, 3, 4)
gc.get_threshold()
gc.set_threshold()
gc.get_threshold()
gc.set_th
