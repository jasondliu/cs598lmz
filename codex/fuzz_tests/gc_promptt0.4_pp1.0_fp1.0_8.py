import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

# Create a bunch of objects.
for i in range(10):
    exec("a%d = range(10)" % i)

# Create a bunch of weakrefs to them.
for i in range(10):
    exec("b%d = weakref.ref(a%d)" % (i, i))

# Create a cycle.
a10 = [a0]
b10 = weakref.ref(a10)
a0.append(a10)

# Collect and check that everything is collected.
gc.collect()
for i in range(11):
    exec("assert b%d() is None" % i)
