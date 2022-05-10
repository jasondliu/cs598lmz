import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class TestObject1(object):
    pass

class TestObject2(object):
    pass

o = TestObject1()
wr = weakref.ref(o)
print wr() is o

del o
gc.collect()
print wr() is None

# Test gc.get_referents()
o1 = TestObject1()
o2 = TestObject2()
o1.o2 = o2

refs = gc.get_referents(o1)
print o1 in refs
print o2 in refs
print len(refs) == 2

# Test gc.get_referrers()
refs = gc.get_referrers(o2)
print o2 in refs
print o1 in refs
print len(refs) == 1

# Test gc.get_objects()
objs = gc.get_objects()
print o1 in objs
print o2 in objs
print len([o for o in objs if type(o) is TestObject1]) > 1

# Test
