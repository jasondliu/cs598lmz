import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable() with weakrefs
import gc, weakref
class Foo:
    def __del__(self): pass
    def __repr__(self): return '<Foo object>'
    pass
o = Foo()

# o is uncollectable
del o
gc.collect()
# returns 1 if uncollectable, 0 if collectable
print(gc.is_tracked(o))
print(gc.is_tracked(object()))
print(gc.get_count())
print(gc.get_threshold())
gc.set_threshold(300,10,10)
print(gc.get_threshold())
x = Foo()
print(gc.garbage)
del x
print(gc.garbage)
gc.collect()
print(gc.garbage)
print(gc.get_referrers(gc.garbage[0]))
print(gc.get_objects())
print(gc.get_stats())
a = gc.get_objects()
for obj in a:
    print(obj)
print(gc.get_refer
