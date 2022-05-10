import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() to make sure it clears weakrefs
def f():
    class C:
        pass
    x = C()
    x.a = x
    wr = weakref.ref(x)
    del x
    gc.collect()
    print wr()
    return wr
wr = f()
wr()

# Test gc.collect() to make sure it clears weakrefs
def f():
    class C:
        pass
    x = C()
    x.a = x
    wr = weakref.ref(x)
    del x
    gc.collect()
    print wr()
    return wr
wr = f()
wr()

# Test gc.collect() to make sure it clears weakrefs
def f():
    class C:
        pass
    x = C()
    x.a = x
    wr = weakref.ref(x)
    del x
    gc.collect()
    print wr()
    return wr
wr = f()
wr()

# Test gc.collect() to make sure it clears weakrefs
def f
