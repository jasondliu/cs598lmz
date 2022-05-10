import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() doesn't crash
gc.collect()

# Test gc.get_threshold()
print(gc.get_threshold())

# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)
print(gc.get_threshold())
# Test gc.set_threshold() with bad parameters
try:
    gc.set_threshold("1")
except TypeError:
    pass
else:
    print("gc.set_threshold() didn't raise TypeError")
try:
    gc.set_threshold(1, 2)
except ValueError:
    pass
else:
    print("gc.set_threshold() didn't raise ValueError")
try:
    gc.set_threshold(0, 1, 2)
except ValueError:
    pass
else:
    print("gc.set_threshold() didn't raise ValueError")

# Test gc.get_count()
print(gc.get_count())

# Test gc.get_stats()
print(gc.get_stats
