import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
w = weakref.ref(gc.collect())
print(w)
print(w())
del w
gc.collect()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
print(gc.get_debug())
gc.set_debug(gc.DEBUG_STATS)
print(gc.get_debug())
gc.set_debug(gc.DEBUG_LEAK)
print(gc.get_debug())
gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK)
print(gc.get_debug())
gc.set_debug(gc.DEBUG_COLLECTABLE)
print(gc.get_debug())
gc.set_debug(gc.DEBUG_SAVEALL)
print(gc.get_debug())

# Test cyclic gc
class C:
    pass

c1 = C()
c2 = C()
c1.x = c2
c2.x = c1
del c1, c2
gc.collect()

# Issue #2829:
