import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class TestGC:
    def __init__(self):
        print 'Init TestGC'
    def __del__(self):
        print 'Delete TestGC'

a1 = TestGC()
a2 = TestGC()
a3 = TestGC()

a2 = a1
a1 = a3
a3 = a2

del a1
del a2
del a3

gc.collect()

# Test gc.garbage
a1 = TestGC()
a2 = TestGC()
a3 = TestGC()

a2 = a1
a1 = a3
a3 = a2

del a1
del a2
del a3

print gc.garbage

# Test gc.get_referrers
class TestGC2:
    def __init__(self):
        print 'Init TestGC2'
    def __del__(self):
        print 'Delete TestGC2'

a1 = TestGC2()
a2 = TestGC2()
a3 = TestGC2()

a2 = a
