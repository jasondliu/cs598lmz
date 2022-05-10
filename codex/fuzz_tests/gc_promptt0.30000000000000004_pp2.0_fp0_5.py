import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test checks that gc.collect() collects all unreachable objects
# and calls their __del__ methods.

import gc, weakref

class C(object):
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return "<C %d>" % self.n
    def __del__(self):
        print "collecting", self

def f():
    print "creating objects"
    for i in range(6):
        C(i)
    print "collecting"
    n = gc.collect()
    print "collected", n
    print "done"

f()
print "exiting"
