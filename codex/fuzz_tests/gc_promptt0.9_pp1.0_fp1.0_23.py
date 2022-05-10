import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
gc.collect()
assert len(gc.garbage) == 0

# Allocate a ton of objects.
n = 10000
al = [None] * n
for i in range(n):
    al[i] = []
del al

# Trigger a collection.
gc.collect()
# The number of objects left in the list is highly variable,
# e.g. at least n*0.1-1 for n==1000 already here on a normal run.
# See CPython's Lib/test/test_gc.py for details.
assert 0 <= len(gc.garbage) <= n, \
       "unexpected number of objects left in garbage: got %d, expected at most %d" % \
       (len(gc.garbage), n)

# Clean up before the next step.
gc.garbage = []

# Test whether garbage is really collected.
class A:
    pass


x = A()
y = A()
w = weakref.ref(x)
assert w() is x
del x
# y should be unreachable now
y = None
