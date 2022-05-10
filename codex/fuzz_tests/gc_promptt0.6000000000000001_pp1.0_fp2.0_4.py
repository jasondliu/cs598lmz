import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations

# For each generation, we want to create a sequence of objects that
# are uncollectable at each stage.  We can do this by creating a
# sequence of objects that refer to each other, and use a weakref to
# the first one to keep track of the sequence.

# This function creates a sequence of n collectable objects, where
# each object is a pair (x, y), where x is an integer, and y is a
# reference to the previous object in the sequence.  The first object
# in the sequence is (0, None), and the last object is (n-1, first).
# The function also creates a weak reference to the first object in
# the sequence, which is the only reference to the whole sequence
# (thus, the sequence is uncollectable).
def create_objects(n):
    # Create the first object
    first = [0, None]
    # Create a weak reference to the first object
    weak = weakref.ref(first)
    # Create an uncollectable cycle
    for i in range(1, n):
        obj = [i, first
