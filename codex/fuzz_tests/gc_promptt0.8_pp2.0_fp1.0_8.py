import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
for x in range(4):
    print('Testing gc.collect() with objects ... ', end='')
    gc.collect()
    gc.collect()
    gc.collect()
    gc.collect()
    if len(gc.garbage) == len(objects):
        print('ok')
    else:
        print('failed')
    gc.garbage[:] = []

# Test gc.collect()
for x in range(4):
    print('Testing gc.collect() with refs ... ', end='')
    gc.collect()
    gc.collect()
    gc.collect()
    gc.collect()
    if len(gc.garbage) == len(refs):
        print('ok')
    else:
        print('failed')
    gc.garbage[:] = []

# Test gc.garbage
for x in range(4):
    print('Testing gc.garbage with objects ... ', end='')
    gc.garbage[:] = []
    if len(
