import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.collect(2).  Also tests the garbage collector's
# ability to collect a list of objects with a cycle.  This test assumes that
# gc.collect() and gc.collect(2) return the number of objects collected and
# uncollectable.

class C:
    pass

def check_stats(label, dict, list, uncollectable, collected=0):
    if gc.get_count() != (dict, list, uncollectable):
        print "%s: wrong gc.get_count()" % label
    if len(gc.garbage) != uncollectable:
        print "len(gc.garbage) != uncollectable after %s" % label
    if gc.collect() != collected:
        print "gc.collect() != collected after %s" % label
    if gc.collect(2) != uncollectable:
        print "gc.collect(2) != uncollectable after %s" % label
    if len(gc.garbage) != 0:
        print "len(gc.garbage) != 0 after %
