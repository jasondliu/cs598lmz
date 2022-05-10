import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a couple of objects that share a reference.
# The first is a list, which is mutable.
# The second is a tuple, which is immutable.
# The list is forced to a particular size, which happens to be the
# default threshold for the number of objects before gc kicks in.
# The purpose is to make it possible to predict the number of objects
# created.

def new_list():
    l = [None] * 10
    l.append(new_list)
    return l

def new_tuple():
    t = ([],)
    return t

bases = []
for i in range(10):
    bases.append(new_list())
    bases.append(new_tuple())

a = bases[0]
b = bases[1]

# Set up the circular references.

for i in range(0, len(bases), 2):
    bases[i].append(bases[i+1])
    bases[i+1][0].append(bases[i])

# Now delete the bases to force g
