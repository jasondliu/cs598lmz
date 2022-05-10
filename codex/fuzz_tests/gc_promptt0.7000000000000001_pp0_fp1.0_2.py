import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on a weakref to a class instance.

class C:
    pass

def callback(*args):
    print "called back"

ob = C()
ref = weakref.ref(ob, callback)

print ob
print "ref", ref
print "hash", hash(ob)
print "id", id(ob)

del ob
print "collecting"
gc.collect()
print "done"

print "expecting callback"
import gc
gc.collect()
print "done"
