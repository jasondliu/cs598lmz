import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

# Create a bunch of objects that refer to each other
# and then create a cycle.

class C:
    pass

ob1 = C()
ob2 = C()
ob1.x = ob2
ob2.x = ob1
ob3 = C()
ob3.x = ob3

# Create a weakref to ob1

wr = weakref.ref(ob1)

# Enter ob1 in a cycle

l = [ob1]

# At this point, ob1 is uncollectable, but ob2 and ob3 are collectable

gc.collect()

assert wr() is ob1
assert gc.collect() == 2
assert wr() is ob1

# Break the cycle

del l

# At this point, ob1 and ob2 are collectable, but ob3 is not

gc.collect()

assert wr() is ob1
assert gc.collect() == 1
assert wr() is ob1

# Break the cycle involving ob3

del ob3

# Now, everything is collectable


