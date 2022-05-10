import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() directly
gc.collect()
# Test with printing enabled
gc.set_debug(gc.DEBUG_STATS)
gc.collect()

# Run cyclic gc directly
gc.collect()

# Test with printing enabled
gc.set_debug(gc.DEBUG_SAVEALL)
gc.collect()

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()

class Foo:
    a = None
    def __init__(self):
        pass

gc.set_debug(gc.DEBUG_SAVEALL)
foo = Foo()

v = gc.get_referents(foo)
w = gc.get_referrers(foo)

# disabled due to "free" from _PyObject_Free, which confuses cpychecker
#gc.set_debug(gc.DEBUG_STATS)
bar = Foo()
del bar

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
foo = Foo()
v = gc.get_referents(foo)
w = gc.
