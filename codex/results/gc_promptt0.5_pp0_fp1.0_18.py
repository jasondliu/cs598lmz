import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
#
# This tests the case where a weakref is created to an object that
# is already dead.  It is important to make sure that the weakref
# itself is collected.  This test checks that the weakref callback
# is not called.  It also checks that the weakref object is
# collected in the next collection.

class C:
    pass

def callback(wr, self=weakref.ref(C)):
    print "callback"
    print wr() is self()

def main():
    c = C()
    wr = weakref.ref(c, callback)
    del c
    gc.collect()
    print wr() is None
    print wr() is None

main()
