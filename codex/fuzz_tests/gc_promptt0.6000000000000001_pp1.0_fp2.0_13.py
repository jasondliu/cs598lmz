import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f1():
    import gc
    a = []
    a.append(a)
    b = []
    b.append(b)
    a.append(b)
    b.append(a)
    del a, b
    gc.collect()
    # Should only collect one reference
    return gc.collect()

print(f1())
# Test gc.collect() with cyclic trash and uncollectable objects
def f2():
    import gc
    a = []
    b = []
    a.append(b)
    b.append(a)
    c = [a, b]
    del a, b
    gc.collect()
    # Should collect two references
    return gc.collect()

print(f2())
# Test gc.collect() with cyclic trash and collectable objects
def f3():
    import gc
    a = []
    b = []
    a.append(b)
    b.append(a)
    c = [a, b]
    del a, b
   
