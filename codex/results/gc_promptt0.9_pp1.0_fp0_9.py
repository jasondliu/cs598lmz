import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
gc.collect()
# Test gc.get_referrers().
a = []
a.append(a)
gc.get_referrers(a)

# Test gc.get_referents().
gc.get_referents(a)

# Test gc.get_objects().
i = 0
b = object()
while b in gc.get_objects():
    i = i + 1
    b = object()
i

# Test gc.get_stats().
stats = gc.get_stats()
# Seems enough for now
stats['collected'], stats['uncollectable']

# Test gc.is_tracked().
gc.is_tracked(a)
w = weakref.ref(a)
gc.is_tracked(w)
gc.collect()
gc.is_tracked(w)

## Test gc flags
gc.DEBUG_STATS
gc.DEBUG_STATS == gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | \
    gc.DEBUG
