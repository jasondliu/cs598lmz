import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

# Make sure that gc.collect() clears the weakrefs dictionary
# and that it doesn't clear unreachable objects.

# Note:  This test is not run automatically.  It must be run
# manually by the user.

class C:
    pass

def callback(wr):
    print "callback"

c = C()
wr = weakref.ref(c, callback)
print wr() is c
print gc.collect()
print wr() is c
del c
print gc.collect()
print wr()
print gc.collect()
print wr()
print gc.collect()
print wr()
print gc.collect()
print wr()
print gc.collect()
print wr()
print gc.collect()
print wr()
print gc.collect()
print wr()
print gc.collect()
print wr()
print gc.collect()
print wr()
print gc.collect()
print wr()
print gc.collect()
print wr()
print gc.collect()
print wr()
print g
