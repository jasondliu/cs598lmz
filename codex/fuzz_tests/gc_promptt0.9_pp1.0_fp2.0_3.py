import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
gc.collect()
gc.collect()
gc.collect()
# Figure out garbage cycle debugging
import gc
class C:
    def __init__(self):
        pass
    def __del__(self):
        print "Object deleted."
gc.disable()
print "Creating instances: "
c1 = C()
c2 = C()
print "List of inst. reachable from the loop:", gc.get_referrers(c2)
L = [C(), C(), 5]
print " Making loop... ",
c1.next = c2
c2.next = c1
del c1, c2
L.append(L)
gc.collect()
print "List of inst. unreachable from the loop: ", gc.get_referrers(L)
print "Re-enabling collector..."
del L
gc.enable()
gc.collect()
# Test trashcan
import gc
gc.disable()
class C:
    def __del__(self):
        print "C.__del__"
def shrink():
    print "Trashcan
