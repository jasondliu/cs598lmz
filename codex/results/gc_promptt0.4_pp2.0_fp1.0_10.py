import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a bunch of objects that are not collectable.
# The first one is a list, which is a container.
# The rest are strings, which are not containers.

# The list contains a reference to each string.
# The string's reference count is 2, one for the list and one for
# the name of the variable.

# Note that these strings are not interned.  Interned strings
# are not collected.

a = []
for i in range(10):
    exec("s%d = 'x' * 100000" % i)
    exec("a.append(s%d)" % i)

# Now delete the list.
del a

# The strings' reference count should be 1 now.
# The list is gone, but the names s0, s1, etc. still exist.

gc.collect()

# Now delete the names.

for i in range(10):
    exec("del s%d" % i)

# The strings' reference count should be 0 now,
# so they should get collected.

gc.collect()


