import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
for i in range(5):
    print('gc.collect(%d):' % i, end=' ')
    n = gc.collect(i)
    print(n)
print(gc.garbage)
