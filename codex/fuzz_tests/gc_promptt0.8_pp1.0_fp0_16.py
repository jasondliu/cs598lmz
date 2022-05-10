import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(2)
a = []
b = []
# This test is no longer guaranteed to run any destructors, so it's
# not a great test of collect(2) correctness.  However, it can still
# detect some egregious problems.
#print "Collecting", gc.collect(2)
#print "Done collecting"
#print gc.garbage
#print "Collecting", gc.collect(2)
#print "Done collecting"
del a
gc.collect()

# Test issue8106
for i in range(100):
    a = []
    b = [a]
    c = [a]
    a.append(b)
    a.append(c)
    del a, b, c
gc.collect()
a = []
b = [a]
c = [a]
a.append(b)
a.append(c)
del c
gc.collect()
del a, b
gc.collect()

# Check gc.DEBUG_SAVEALL
gc.set_debug(gc.DEBUG_SAVEALL)
gc_collect_
