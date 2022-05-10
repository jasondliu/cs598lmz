import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
print 'gc.get_count()                 :', gc.get_count()
print 'gc.get_referrers(wr)           :', gc.get_referrers(wr)
print 'gc.get_referrers(a)            :', gc.get_referrers(a)
print 'gc.get_referents(a)            :', gc.get_referents(a)
print 'gc.get_referents(b)            :', gc.get_referents(b)
print

# Test gc.garbage collection
print 'gc.garbage                      :', gc.garbage
print

# Test gc.get_referrers and gc.get_referents
l = [1,2]
print 'gc.get_referrers(l)             :', gc.get_referrers(l)
print 'gc.get_referents(l)             :', gc.get_referents(l)
print

def
