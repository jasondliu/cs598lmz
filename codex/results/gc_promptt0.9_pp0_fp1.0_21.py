import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect w/o TWEAK_HEURISTIC2
gc.set_threshold(1, 1, 1)

#
# Return the list of objects reachable (directly or indirectly) from x.
#

def get_r(x):
    gc.collect()
    res = gc.get_referrers(x)
    gc.collect()
    return res

#
# Test gc.collect w/ TWEAK_HEURISTIC2
#
gc.set_threshold(0,0,0)

def get_r_heuristic(x):
    gc.collect()
    res = gc.get_referrers(x)
    gc.collect()
    return res

class X(object):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return repr(self.id)

#
# Create separate objects from which x is reachable
#

def rgc():
    l = []
    for x in get_r(l):
