import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with references.
# Method for testing garbage-collected objects:


def test(o):
    print('Testing:', o)
    print('  Referenced by:', wr(o).ref())
    print('  Length of weak reference list:', len(wr(o).weakreflist))
    print('  Is the object alive:', bool(wr(o).ref()))
    print('  Is the object collectable:', wr(o).weakreflist is not None)


w = weakref.WeakValueDictionary()
u = weakref.WeakKeyDictionary()
# Test we can create a large number of small objects, handle circular
# references and key errors all at the same time.
print('\nTesting object with simply cyclic references:')
a = [object() for i in range(10)]
for i in range(-10, -1):
    a[i] = a[i + 1]


print('  a is:', a)
a = None
print('  Now a is:', a)
print('  Is test(a) live:', bool(
