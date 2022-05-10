import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage
def test():
    # Test collect
    g = [gc.garbage, weakref.ref(gc.garbage), lambda:None]
    g[1]()
    g[2] = g
    del g[1]
    del g[2]
    gc.collect()
    gc.garbage.append(g)
    gc.collect()
test()
print gc
