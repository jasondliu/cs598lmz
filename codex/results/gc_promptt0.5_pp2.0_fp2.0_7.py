import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []
for i in range(10):
    a.append(i)
    gc.collect()
    print(gc.collect())
    print(gc.garbage)

# Test gc.get_threshold()
print(gc.get_threshold())

# Test gc.get_count()
print(gc.get_count())

# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
print(gc.get_threshold())

# Test gc.is_tracked()
print(gc.is_tracked(a))

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)

# Test gc.DEBUG_STATS
gc.set_debug(gc.DEBUG_STATS)

# Test gc.DEBUG_SAVEALL
gc.set_debug(gc.DEBUG_SAVEALL)
gc.collect()
print(gc.garbage)

# Test gc.DEBUG_LEAK
gc.set_debug
