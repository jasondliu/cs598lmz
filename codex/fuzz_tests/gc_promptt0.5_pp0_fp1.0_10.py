import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
class E:
    pass
for o in [A, B, C, D, E]:
    o.__module__ = 'm'
gc.collect()
gc.collect()
print(gc.garbage)
del A, B, C, D, E
gc.collect()
print(gc.garbage)
# Test gc.get_referrers()
class X(object):
    pass
class Y(object):
    pass
x = X()
y1 = Y()
y2 = Y()
x.attr = y1
y1.attr = y2
y2.attr = x
del x, y1, y2
gc.collect()
print(gc.garbage)
# Test gc.get_referents()
# Test gc.is_tracked()
class X(object):
    pass
x = X()
print(gc.is_tracked(x))
del x
