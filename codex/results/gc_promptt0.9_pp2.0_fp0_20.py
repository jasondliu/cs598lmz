import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.get_referrers()

class A:
    pass
a = A()
print 'gc.collect()'
gc.collect()
print 'collectable: ROOT + a->get_referrers():', gc.collect()
print 'get_referrers(a):', gc.get_referrers(a)
print

print 'del a'
del a
print 'gc.collect()'
gc.collect()
print 'collectable: ROOT + a->get_referrers():', gc.collect()
print

print 'a = A()'
a = A()
print 'gc.collect()'
gc.collect()
print 'collectable: ROOT + a->get_referrers():', gc.collect()
print 'get_referrers(a):', gc.get_referrers(a)
print

print 'del a'
del a
print 'gc.collect()'
gc.collect()
print 'collectable: ROOT + a->get_referrers():', gc.collect()

