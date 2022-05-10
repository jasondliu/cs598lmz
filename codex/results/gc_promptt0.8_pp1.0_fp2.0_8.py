import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
L = []
for i in range(5):
    L.append(gc.collect())
assert L == [2, 2, 2, 2, 2]
# Test gc.garbage
if verbose:
    print('From now on, expect a gc.garbage message')
gc.collect()
gc.collect()
if verbose:
    print('Done')
# Test cyclic garbage with no deallocation
if verbose:
    print('Expect 5 messages')
for i in range(5):
    if verbose:
        print('Pass #', i)
    L = []
    L.append(L)
    del L
    gc.collect()
    if verbose:
        print('Done.')
if verbose:
    print('Expect a message for each of 10 objects')
for i in range(10):
    if verbose:
        print('Creating object number ', i)
    L = []
    L.append(gc.collect)
if verbose:
    print('Done.')
# Test uncollectable objects with no deall
