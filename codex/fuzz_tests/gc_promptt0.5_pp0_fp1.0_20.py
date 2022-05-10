import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class Derived(object):
    pass

class Base(object):
    def __init__(self):
        self.derived = Derived()

def make_cycle():
    b = Base()
    b.derived.base = b

make_cycle()
gc.collect()
# This should have triggered a collection
print gc.collectable()
# But the objects are still alive
print gc.is_tracked(Derived())
print gc.is_tracked(Base())
# The weakref module is not affected by this
r = weakref.ref(Derived())
print r() is None
# Test gc.get_referents()
l = []
l.append(l)
gc.collect()
print gc.get_referents(l)
# Test gc.get_referrers()
print gc.get_referrers(l)
# Test gc.get_objects()
print gc.get_objects()
# Test gc.get_stats()
print gc.get_stats()
# Test g
