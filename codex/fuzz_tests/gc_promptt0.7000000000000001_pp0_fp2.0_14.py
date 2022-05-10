import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C:
    pass

c = C()
d = weakref.ref(c)
print d
gc.collect()
print d

#Test gc.get_referrers()
class C:
    pass

c = C()
d = weakref.ref(c)

gc.collect()

print repr(gc.get_referrers(c)).replace('L', '')
print repr(gc.get_referrers(d)).replace('L', '')

# Test gc.get_objects()
class C:
    pass

c = C()
d = C()

gc.collect()

objs =  gc.get_objects()
print objs.count(c), objs.count(d)
print c in objs, d in objs

# Test gc.get_stats()
gc.collect()
print gc.get_stats()

# Test gc.set_threshold()
gc.collect()
gc.set_threshold(1000)
print gc.get_threshold()
