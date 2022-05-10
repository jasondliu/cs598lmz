import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Make a data structure that's cyclic and test it
# Also create a weakref to it
l = []
l.append(l)
r = weakref.ref(l)

# Create a large data structure
l = []
for i in xrange(10):
    l = [l] * 1000

# Check that we have a cyclic data structure
if not r():
    print "Error, cyclic data structure doesn't work"
    exit(1)
else:
    print "Cyclic data structure works!"

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

# Collect garbage (should only delete the big structure)
# and print what got collected
print "Collecting ..."
gc.collect()
for i in gc.garbage:
    print i
gc.garbage = []
