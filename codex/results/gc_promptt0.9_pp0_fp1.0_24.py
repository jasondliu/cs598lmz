import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
gc.collect()

# loop on any kind of garbage
# permanent garbage
a, b, c, d, a1, a2, a3 = 1, 'hello', "world", {}, {}, {}, []
# tuncated references
a4 = [1]
a4.append(a4)
a5 = []
a5.append(a5)
# take proper care of the flagged cyclic garbage
print(gc.collect())

# Print the uncollectable objects found
print()
print('Uncollectable:')
for o in gc.garbage:
    print(o)
    del o
del gc.garbage[:]

# non-tuncated cycles
#   several multi-level permutations to catch all possible orders
#   possibly get a little more tricky
# non-tuncate cycle with self-reference
q1 = []
q1.append(q1)

# dictionary with cyclic reference:
d = {}
d[1] = d
print(gc.collect())

# dictionary with self-reference:
d = {}
d
