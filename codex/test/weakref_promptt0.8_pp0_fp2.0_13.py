import weakref
# Test weakref.ref by creating a bunch of objects that refer to each other,
# and deleting the reference to the first object in the chain.  The objects
# should all be garbage-collected, even though they contain cyclic structures.
#
# Note that this test takes a long time to run.

class C:
    pass

N = 100

# Create a bunch of objects that refer to each other circularly.
objects = []
for i in range(N):
    c = C()
    objects.append(c)
    # Make the new object refer to the previous one.
    if objects[i-1]:
        c.cycle = objects[i-1]

# Clear the reference to the first object in the chain.
objects[0] = None

# Store a bunch of weak references to the objects, in a variety of data
# structures.
wlist = []
for obj in objects:
    wlist.append(weakref.ref(obj))

wset = set()
for obj in objects:
    wset.add(weakref.ref(obj))

wdict = {}
