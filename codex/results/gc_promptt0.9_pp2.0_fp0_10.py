import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    dlist = []
    for x in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
        dlist.append(( weakref.ref(dlist), x))
    def x():
        return
    x1 = x
    x = 1
    del x1
    dlist.append(dlist)
    del dlist

f()
gc.collect()


print
# Test gc.get_referents()
#
# Interesting cases:
#
# - tuples of weakrefs (weakref.py)
#
# - tuples that contain cycles including some objects with __del__
#   methods and some weakrefable objects (e.g. a tuple that contains
#   a list and a weakref to that list).  (This was prompted by a bug
#   in cPickle.py.)
d1list = []
d2list = []
def g():
    # Create a list with a cycle in it
