import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations
gc.collect()
# collect_generations collects only objects with refcount < 2
gc.collect_generations()

class A:
    pass

a = A()
a = weakref.ref(a)
gc.collect()

# collect_generations collects all objects
gc.collect_generations()

# collect_generations collects only objects with refcount < 2
gc.collect_generations()

# collect_generations collects all objects
gc.collect_generations(2)

a = weakref.ref(A())
gc.collect()

# collect_generations collects only objects with refcount < 2
gc.collect_generations()

# collect_generations collects all objects
gc.collect_generations(2)

gc.set_debug(0)

# Verify that gc.collect() clears the generation0
gc.collect(0)
gc.collect_generations()

# Check that gc.collect() clears generation0, generation1 and generation2
gc.collect(2)
gc.collect_generations()

gc
