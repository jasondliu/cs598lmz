import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def callback(o):
    print "collected", o

def callback1(o):
    print "collected1", o


def test_callback():
    l = []
    for i in range(10):
        x = weakref.ref(l, callback)
        y = weakref.ref(l, callback1)
        print "x", x, "y", y
        del l
        gc.collect()
        print "x", x, "y", y
        l = [1, 2, 3, 4]

# Test gc.collect()
def test_callback1():
    l = []
    for i in range(10):
        x = weakref.ref(l, callback)
        y = weakref.ref(l, callback1)
        print "x", x, "y", y
        del l
        gc.collect()
        print "x", x, "y", y
        l = [1, 2, 3, 4]
        gc.collect()
        print "x", x, "y", y

#
