import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    x = C()
    x.a = x
    l = [x]
    x.l = l
    del x
    gc.collect()

f()
gc.collect()
# Test gc.get_objects()

class C:
    pass

def f():
    x = C()
    x.a = x
    l = [x]
    x.l = l
    del x

f()
gc.collect()

# Test gc.get_referrers()

class C:
    pass

def f():
    x = C()
    x.a = x
    l = [x]
    x.l = l
    del x

f()
gc.collect()

# Test gc.get_referents()

class C:
    pass

def f():
    x = C()
    x.a = x
    l = [x]
    x.l = l
    del x

f()
gc.collect
