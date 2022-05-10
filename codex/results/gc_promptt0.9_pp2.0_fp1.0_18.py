import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Create a list of weak references to ints and tuples
x = []
for i in range(10):
    y = int(i)
    x.append(weakref.ref(y))
# Let's watch our list
import pprint
pprint.pprint(x)

# Now force a full collection
gc.collect()

# Look in our list and see if the reference is gone
pprint.pprint(x)

# If a strong reference was created between the first print of our list
# and the collect, then the second print will show a reference still
# there.  Look at the output after uncommenting the following line
#x.append(y)

# Push out the reference using del
del y

# Now force a full collection
# See if the reference is dead yet
gc.collect()
pprint.pprint(x)

# Let's do it again, this time to a tuple
x = []
for i in range(10):
    y = (int(i), int(i*i))
    x.append(weakref.ref(y
