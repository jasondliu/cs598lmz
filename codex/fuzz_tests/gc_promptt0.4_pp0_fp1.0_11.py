import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# The following test is known to fail on some platforms.  It is
# unclear whether this is a Python bug or a bug in the platform's
# garbage collector.  If you know which is the case, please let us
# know.

class C:
    def __init__(self, n):
        self.n = n

def callback(ignored):
    print "callback!"

def test(n):
    print "test(%s)" % n
    # Create a cycle, and make sure it gets collected.
    x = C(n)
    y = C(n)
    x.other = y
    y.other = x
    wr = weakref.ref(x, callback)
    del x, y
    gc.collect()
    if wr() is not None:
        raise TestFailed, "cycle was not collected"

# Check that the cycle is collected when the callback is called.
test(1)

# Check that the cycle is collected even if the callback is
# unregistered.
test(2)

# Check that the cycle is
