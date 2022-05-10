import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
print 'collect:', gc.collect()

# Create a list.  If it is not tracked, the list is immediately
# destroyed, and will disappear off the end of the world.
if gc.isenabled():
    # find instances of instancemethod class
    # to avoid problems in case class instancemethod is defined
    # somewhere else than in types
    imclass = type(len)
    tracked = weakref.WeakKeyDictionary()
    track = tracked.__setitem__
    for o in gc.get_objects():
        if isinstance(o, imclass):
            track(o.im_self)
    class R(object):
        def __init__(self, a):
            self.a = a
        def __repr__(self):
            return "R(%r)" % (self.a,)
    gc.disable()
    try:
        r = R(tracked)
    finally:
        gc.enable()
    #print "r:", r
    a = r.a
    #print a
    del r
    #
