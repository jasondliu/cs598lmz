import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# Create a cycle with a finalizer that can't be run.
#
# We use a weakref to prevent the cycle from being collectable,
# and then delete the weakref.  If gc.collect() doesn't clear the
# unreachable finalizer, the object will be resurrected when
# the weakref is deleted.

class C:
    def __del__(self):
        print "del"

def check(x):
    print "checking", x
    if x is not None:
        print "FAILED"

def main():
    c = C()
    c.x = c
    r = weakref.ref(c)
    del c
    gc.collect()
    check(r())
    del r
    gc.collect()
    check(r())

main()
