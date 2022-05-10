import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C:
    pass

def test():
    a = C()
    a.b = C()
    a.b.a = a
    del a

test()
gc.collect()

# Test gc.garbage
class C:
    pass

def test():
    a = C()
    a.b = C()
    a.b.a = a
    del a
    return a

gc.garbage.append(test())
gc.collect()

# Test gc.get_objects()
class C:
    pass

def test():
    a = C()
    a.b = C()
    a.b.a = a
    del a
    return a

test()
gc.collect()

# Test gc.get_referrers()
class C:
    pass

def test():
    a = C()
    a.b = C()
    a.b.a = a
    del a
    return a

test()
gc.collect()

# Test gc.get_ref
