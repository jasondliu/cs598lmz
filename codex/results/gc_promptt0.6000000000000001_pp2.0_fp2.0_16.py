import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print "gc.collect()", gc.collect()

print "gc.get_referrers of module", gc.get_referrers(sys.modules)
print "gc.get_referrers of sys.modules[__main__]", gc.get_referrers(sys.modules['__main__'])
print "gc.get_referrers of sys.modules[__main__].__dict__", gc.get_referrers(sys.modules['__main__'].__dict__)

# Test gc.get_objects()
print "gc.get_objects()", len(gc.get_objects())

# Test gc.get_debug()
print "gc.get_debug()", gc.get_debug()

# Test gc.is_tracked()
print "gc.is_tracked()", gc.is_tracked(sys)

# Test gc.get_threshold()
print "gc.get_threshold()", gc.get_threshold()

# Test g
