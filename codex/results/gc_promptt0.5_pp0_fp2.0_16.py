import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo:
    def __del__(self):
        print 'Foo.__del__'

f = Foo()

gc.collect()

print gc.collect()

f = None

gc.collect()

print gc.collect()

del f

gc.collect()

print gc.collect()

# Test gc.get_threshold()
print gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(2, 3, 4)

print gc.get_threshold()

# Test gc.get_count()
print gc.get_count()

# Test gc.get_debug()
print gc.get_debug()

gc.set_debug(gc.DEBUG_STATS)

# Test gc.set_debug()
print gc.get_debug()

gc.set_debug(gc.DEBUG_LEAK)

print gc.get_debug()

gc.set_debug(0)

print g
