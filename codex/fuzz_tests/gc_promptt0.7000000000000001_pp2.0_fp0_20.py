import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class C(object):
    pass

def callback(w):
    print "callback"

def f():
    x = C()
    x.selfref = x
    wr = weakref.ref(x, callback)
    print wr     # should produce 'callback'
    del x
    # this next line is important, because it
    # causes x to be collected, and that in turn
    # causes the callback to be invoked
    gc.collect()


f()

# Test gc.get_objects()
gc.collect()
print len(gc.get_objects())

# Test gc.get_referrers()
gc.collect()
print len(gc.get_referrers(gc.get_objects()))

# Test gc.get_referents()
gc.collect()
print len(gc.get_referents(gc.get_objects()))

# Test gc.get_count()
gc.collect()
print gc.get_count()
