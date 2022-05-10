import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without anything to collect
gc.collect()
print("gc.collect: collected and unreachable should be both 0", gc.collect())

# Test gc.collect() with something to collect, but unreachable
counts = gc.get_count()
# Create a chain of objects with length == counts[0] + 1
tail = []
for i in range(counts[0] + 1):
    head = [tail]
    if i > 0:
        tail[0] = head
    tail = head
del i, head, tail
gc.collect()
print("gc.collect: collected and unreachable should be both 1", gc.collect())

# Test gc.collect() with something to collect, including a reachable
# cycle, and some unreachable (including a cycle).
w = []
wref = weakref.ref(w)
gc.collect()
print("gc.collect: collected and unreachable should be both 0", gc.collect())
x = []
x.append(x)
y = []
y.append(y)
w = [x, y]
