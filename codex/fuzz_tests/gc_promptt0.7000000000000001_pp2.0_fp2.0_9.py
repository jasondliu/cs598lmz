import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations
gc.collect_generations()
gc.collect_generations() # is idempotent
# gc.collect()
# gc.collect(1) # Not implemented
# gc.collect(0) # Not implemented
# gc.collect(-1) # Not implemented
# gc.collect(1, 1) # Not implemented
# gc.collect(0, 1) # Not implemented
# gc.collect(-1, 1) # Not implemented
# gc.collect(1, 0) # Not implemented
# gc.collect(1, -1) # Not implemented
class C:
    pass
c = C()
c.a = C()
c.a.a = c
c.b = c.a
print gc.collect_generations()
print gc.get_referrers(c)
print gc.get_referrers(c.a)
print gc.get_referrers(c.a.a)
print gc.get_referents(c)
print gc.get_referents(c.
