import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C(object):
    pass

c = C()
print(gc.is_tracked(c))
print(gc.is_tracked(C))
print(gc.is_tracked(C()))
print(gc.get_referrers(c))
print(gc.get_referrers(C))
print(gc.get_referrers(C()))
del c
class D(object):
    pass

d = D()
# print(gc.get_referrers(d))
print(gc.get_referrers(D))
print(gc.get_referrers(D()))
del d
import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
class C(object):
    pass
c = C()
print(gc.get_referrers(c))
print(gc.get_referrers(C))
print(gc.get_referrers(C()))
del c
class D(object):
    pass
d = D()
print(gc.get_
