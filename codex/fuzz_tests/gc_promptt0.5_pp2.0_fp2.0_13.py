import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# Tests that gc.collect() collects everything that is collectable.

import gc, weakref

class A:
    pass

def callback(wr):
    print "callback"

def main():
    gc.set_debug(gc.DEBUG_COLLECTABLE)
    a = A()
    wr = weakref.ref(a, callback)
    gc.collect()
    print gc.collect()
    print len(gc.garbage)
    print wr() is None

main()
