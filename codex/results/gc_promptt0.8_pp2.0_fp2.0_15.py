import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect.
print(gc.collect())
print(gc.collect())
a = gc.collect()
print(a)
b = gc.collect()
print(b)

# Test gc.callbacks.
def callback(phase, info=None):
    print(phase)
    if info:
        print(info)
gc.callbacks.append(callback)

# Test gc.get_stats.
print(gc.get_stats())

# Test gc.get_threshold.
print(gc.get_threshold())

# Test gc.set_threshold.
gc.set_threshold(10, 20, 30)

# Test gc.set_debug.
gc.set_debug(gc.DEBUG_LEAK)

# Verify that there are no objects left.
print(gc.collect())

# Verify that there are no lingering callback objects.
print(gc.collect())

# Verify that there are no lingering objects in the top level 'gc' module.
print(gc.collect())
