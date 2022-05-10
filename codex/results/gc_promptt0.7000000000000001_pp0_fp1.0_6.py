import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Test gc.disable()
gc.disable()
# Test gc.enable()
gc.enable()
# Test gc.get_debug()
gc.get_debug()
# Test gc.get_threshold()
gc.get_threshold()
# Test gc.get_objects()
gc.get_objects()
# Test gc.set_debug()
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
# Test gc.set_threshold()
gc.set_threshold(100, 10, 10)
# Test gc.set_threshold()
gc.set_threshold(700, 10, 10)
# Test gc.garbage
class A:
    def __del__(self):
        print "A.__del__"
        gc.garbage.append(self)
a = A()
b = A()
del a
del b
gc.collect()
##print gc.garbage
# Test weakref.ref()
a = A()
r =
