import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print "gc.collect()"
gc.collect()
print gc.garbage
print
print

# Test if an object is collectable by gc.collect()
print "gc.is_tracked(x)"
x = 1
del x
print gc.is_tracked(x)
print
print

# Test if an object is collectable with weakref.ref()
print "weakref.ref(x)"
x = 1
del x
print weakref.ref(x)
print
print

# Test weakref.ref() with callback
print "weakref.ref(x, callback)"
def cb(a):
	print "callback:", a
x = 1
weakref.ref(x, cb)
print gc.is_tracked(x)
del x
print gc.is_tracked(x)
print
print

# Test gc.get_referrers()
print "gc.get_referrers(x)"
print gc.get_referrers(x)
print
print

# Test gc
