import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

gc.collect()
a = A()
a.a = a
del a
gc.collect()
# Test gc.get_referrers()

class A:
    pass

gc.collect()
a = A()
a.a = a
gc.collect()
lst = gc.get_referrers(A)
assert len(lst) == 2
assert isinstance(lst[0], dict)
assert isinstance(lst[1], A)
assert lst[1].a is lst[1]
del a
gc.collect()
lst = gc.get_referrers(A)
assert len(lst) == 1
assert isinstance(lst[0], dict)
# Test gc.get_objects()

gc.collect()
before = gc.get_objects()
a = []
b = {}
c = ()
d = 0
e = ''
gc.collect()
after = gc.get_objects()
new = [x for x in after if x not
