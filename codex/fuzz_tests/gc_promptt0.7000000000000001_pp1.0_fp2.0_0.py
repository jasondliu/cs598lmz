import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a cyclic list of tuples.
# This should not cause a segfault.
class C:
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return "C(%d)" % self.n
    def __del__(self):
        print "deleting", self
        #breakpoint()
# Create a cycle of objects with a __del__ method.
c1 = C(1)
c2 = C(2)
t1 = (c1, c2)
t2 = (c2, c1)
c1.cycle = t2
c2.cycle = t1
# Create a cycle of tuples.
p = []
p.append(p)
# Create a weakref to an object in the cycle.
c1_wr = weakref.ref(c1)
del c1, c2, t1, t2
# Collecting garbage should not crash.
gc.collect()
#print c1_wr()
# Test gc.collect() with a
