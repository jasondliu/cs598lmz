import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test verifies that collect() does actually collect
# unreachable objects.
#
# If the bug is present, this test will print "Cycle was not collected"
# and exit with a failure code.

class A:
    pass

class B:
    pass

a = A()
b = B()

# Create a cycle
a.cycle = b
b.cycle = a

# Remove all references to the objects
a = None
b = None

# Invoke collect()
gc.collect()

# Get a list of all objects still alive
alive = gc.get_objects()

# Check if the cycle was collected
if gc.is_tracked(alive[0]):
    print("Cycle was not collected")
    sys.exit(1)

# Check that the cycle is not tracked anymore
try:
    gc.is_tracked(alive[0])
except ValueError:
    print("OK")
else:
    print("Cycle was not collected")
    sys.exit(1)
