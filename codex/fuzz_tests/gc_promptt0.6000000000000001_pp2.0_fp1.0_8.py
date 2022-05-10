import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(2)
class A:
    pass

a = A()
a.__class__ = A
del A
gc.collect(2)
# Test gc.get_threshold() and gc.set_threshold()
t = gc.get_threshold()
gc.set_threshold(1000, 10, 10)
gc.set_threshold(*t)
# Test gc.get_count()
gc.get_count()
# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(0)
# Test gc.get_debug()
gc.get_debug()
# Test gc.DEBUG_* constants
print(gc.DEBUG_STATS)
print(gc.DEBUG_COLLECTABLE)
print(gc.DEBUG_UNCOLLECTABLE)
print(gc.DEBUG_INSTANCES)
print(gc.DEBUG_OBJECTS)
print(gc.DEBUG_SAVEALL)
print(gc.DEBUG_LEAK)
# Test gc.DEBUG_SAVEALL

