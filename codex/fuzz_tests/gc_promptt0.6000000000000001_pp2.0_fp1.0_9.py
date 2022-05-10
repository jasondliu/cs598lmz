import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect returns the number of unreachable objects
# that have been collected.
class C1:
    pass
class C2:
    pass

class C3:
    def __del__(self):
        print "C3.__del__ called"

def test_gc_collect(count):
    # Create some objects
    l = []
    for i in xrange(count):
        l.append(C1())
    l.append(C2())
    l.append(C3())
    del l
    # Collect unreachable objects
    n = gc.collect()
    # Check number of unreachable objects that have been collected
    return n

assert test_gc_collect(10) == 2

# Test gc.collect returns the number of unreachable objects
# that have been collected.
class C1:
    pass
class C2:
    pass

class C3:
    def __del__(self):
        print "C3.__del__ called"

def test_gc_collect(count):
    # Create some objects
    l = []
   
