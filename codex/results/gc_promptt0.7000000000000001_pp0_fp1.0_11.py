import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs
# Create a bunch of stuff reachable from a list
# Create a bunch of cycles containing a list
# See if we can collect it all

# Create a list of stuff
NUMBER = 250
stuff = []

for i in range(NUMBER):
    # If i is a multiple of 23 put it in a cycle
    if (i % 23) == 0:
        stuff.append(stuff)
    else:
        stuff.append(str(i))

del i

# Create a bunch of cycles
cycles = []
for i in range(NUMBER):
    x = []
    x.append(x)
    cycles.append(x)

# Make the cycles reachable from the stuff
for x in cycles:
    stuff.append(x)

# Create a bunch of weak references to the stuff
refs = []
for x in stuff:
    refs.append(weakref.ref(x))

# Delete the stuff
stuff = None

# Collect!
gc.collect()

# Check that everything has been collected
for wr in refs:

