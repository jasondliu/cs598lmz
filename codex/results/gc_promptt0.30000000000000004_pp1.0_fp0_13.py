import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect()

# Test gc.get_referrers()
gc.collect()

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a

def check_referrers(obj, referrers):
    r = gc.get_referrers(obj)
    assert len(r) == len(referrers)
    for ref in referrers:
        assert ref in r

check_referrers(a, [{'a': a, 'b': b}])
check_referrers(b, [{'a': a, 'b': b}])
del a
del b
gc.collect()

# Test gc.get_referents()
gc.collect()

class A:
    pass

a = A()
b = A()
a.b = b
b
