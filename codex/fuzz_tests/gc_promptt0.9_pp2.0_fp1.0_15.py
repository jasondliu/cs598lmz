import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
r = weakref.ref(gc.collect())
assert r() is not None
# Test gc.garbage.
gc.garbage.append(None)
del r
gc.collect()
assert gc.garbage == []
del gc.garbage[:]
gc.collect()
assert gc.garbage == []

# Just collect objects that should get collected during this test.
gc.collect()

if gc.isenabled():
    for i in range(4):
        if gc.isenabled():
            gc.disable()
        if not gc.isenabled():
            gc.enable()
        gc.collect()
    if gc.isenabled():
        gc.disable()
    gc.collect()

    # Test gc.get_threshold().
    gc.collect()
    prev = gc.get_threshold()
    gc.set_threshold(100, 10, 10)
    gc.collect()
    assert gc.get_threshold() == (100, 10, 10)
    g
