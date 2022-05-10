import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class MyObject:
    def __init__(self):
        self.x = MyObject()
        self.y = weakref.ref(self)

gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.collect()
gc.set_threshold(3)
o = MyObject()
gc.collect()
del o
gc.collect()

# Test gc.disable() / gc.enable()

gc.disable()
gc.enable()

# Test gc.get_debug()

gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.get_debug()

# Test gc.get_count()

gc.get_count()

# Test gc.get_stats()

gc.get_stats()

# Test gc.get_threshold()

gc.get_threshold()

# Test gc.set_debug()

gc.set_debug(gc.DEBUG_COLLECTABLE)

# Test gc.set_threshold()

gc.set_threshold(
