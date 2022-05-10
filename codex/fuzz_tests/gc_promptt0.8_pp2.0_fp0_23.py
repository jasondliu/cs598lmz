import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class X(object):
    pass

class Y(object):
    pass

o = X()
o.x = o
o.y = Y()
o.y.x = o.y

i = o
j = o.y

del o
del o.y

gc.collect()

print gc.collect()
print gc.garbage
print len(gc.garbage)
print len(gc.get_referrers(i))
print len(gc.get_referrers(j))

gc.garbage.pop().x

print gc.collect()
print gc.garbage
print len(gc.garbage)
print i, j
print len(gc.get_referrers(i))
print len(gc.get_referrers(j))

# Test gc.collect(generation)
gc.garbage = []

gc.set_threshold(1, 0, 0)
o = X()
o.x = o
gc.collect(0)

gc.garbage.pop().x
