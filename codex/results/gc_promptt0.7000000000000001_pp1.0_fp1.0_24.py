import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when the "cycle" is on the stack.
# See also test_gc.py:test_del_on_unreachable_but_cyclic().

gc.collect()
print gc.collect()
class C(object):
    def __del__(self):
        print "del", self

c = C()
del c
print gc.collect()
print gc.collect()
