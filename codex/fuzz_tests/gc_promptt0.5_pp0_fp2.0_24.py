import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __del__(self):
        print "A.__del__"

a = A()
a.b = A()
a.b.c = a
del a
gc.collect()

# Test gc.garbage
class C:
    pass

gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.garbage.append(C())
gc.collect()

# Test gc.get_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.get_debug()

# Test gc.get_count()
gc.get_count()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_LEAK)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.set_debug(gc
