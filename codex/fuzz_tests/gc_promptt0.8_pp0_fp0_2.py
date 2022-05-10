import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and gc.garbage
gc.collect()
l = []
for o in gc.garbage:
    print o
    o.append(1)
    l.append(o)
gc.collect()
for o in l:
    print o

gc.set_threshold(0, 0, 0)
gc.collect()
l = []
for o in gc.garbage:
    print o
    o.append(1)
    l.append(o)
gc.collect()
for o in l:
    print o

# Test cyclic garbage
gc.set_debug(gc.DEBUG_COLLECTABLE|gc.DEBUG_UNCOLLECTABLE)
gc.set_threshold(1, 1, 1)

gc.collect()
gc.collect()

l1 = []
l2 = [l1, l1]
del l1
del l2
gc.collect()
gc.collect()

class A:
    pass

gc.collect()
gc.collect()

a = A()
a.x = a
del a

