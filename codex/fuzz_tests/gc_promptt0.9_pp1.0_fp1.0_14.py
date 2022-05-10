import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
print "testing gc.collect()...",
gc.collect()
count = gc.collect()
print count, "unreachable objects"
# This should not crash!
gc.collect()
# Test reachability.
o = []
print "testing reachability...",
print gc.is_tracked(o),
print "obj",
o = C()
print gc.is_tracked(o),
print "class",
o = gc.collect()
print "number of unreachable objects", o,
print "testing untracking...",
print gc.is_tracked(o),
l = [1, 2, 3]
print gc.is_tracked(l),
l = gc.collect()
print "number of unreachable objects", l
print gc.is_tracked(l),
print "testing collection of container objects"
refs = []
for i in xrange(200):
    o = []
    o.append(1)
    o.append(2)
    o.append(3)
    o.append(4
