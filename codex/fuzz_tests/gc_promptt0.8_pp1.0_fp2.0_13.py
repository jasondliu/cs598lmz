import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable flag
class A:
    pass

a = A()
gc.collect()
print '%x' % (gc.get_referents(a)[0].__flags__,), gc.get_referents(a)[0].__flags__ & gc.FLAG_COLLECTABLE
print '%x' % (a.__weakref__.__flags__,), a.__weakref__.__flags__ & gc.FLAG_COLLECTABLE

a.attr = A()
gc.collect()
print '%x' % (a.attr.__weakref__.__flags__,), a.attr.__weakref__.__flags__ & gc.FLAG_COLLECTABLE

a.attr.l1 = [A(), A()]
gc.collect()
print '%x' % (a.attr.l1[0].__weakref__.__flags__,), a.attr.l1[0].__weakref__.__flags__ & gc.FLAG_COLLECTABLE
