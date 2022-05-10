import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with growing interleaved small and large allocations
n = 5000
n1 = gc.collect(0)
all = []
il = 50
m = sum = 0
for i in xrange(n):
    if i % il == 0:
        k = min(15, i/il+1)
        x = range(2**k)
        y = range(2**k)
    else:
        k = min(15, (i//il+1)*il-i+1)
        x = range(2**k)
        y = range(2**k)
    w = weakref.ref(x)
    all.append(w)
    x = None
    y = None
    gc.collect()
    n2 = gc.collect(0)
    n3 = gc.collect(1)
    n4 = gc.collect(2)
    if n2 < n1 or n3 < n2 or n4 < n3:
        raise TestFailed, "%d %d %d %d" % (n1, n2, n3,
