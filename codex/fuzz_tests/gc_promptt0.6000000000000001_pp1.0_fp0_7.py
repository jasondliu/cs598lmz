import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    def __del__(self):
        print "A.__del__"
a = A()
print "before collect"
gc.collect()
print "after collect"
# Test gc.garbage
class A:
    def __del__(self):
        print "A.__del__"
a = A()
print "before collect"
gc.collect()
print "after collect"
a = 1
print "before collect"
gc.collect()
print "after collect"
# Test gc.get_debug()
print gc.get_debug()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
print gc.get_debug()
gc.set_debug(gc.DEBUG_STATS)
print gc.get_debug()
gc.set_debug(gc.DEBUG_LEAK)
print gc.get_debug()
gc.set_debug(gc.DEBUG_COLLECTABLE)
print gc.get_debug()
gc.set_debug(0)
print gc.get_debug()
# Test
