import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(w):
    print "callback", w

f = Foo()
w = weakref.ref(f, callback)
print "created", w

print "collecting"
gc.collect()
print "done"

print "callback", w

print "deleting f"
del f
print "collecting"
gc.collect()
print "done"

print "callback", w

print "creating f"
f = Foo()
print "collecting"
gc.collect()
print "done"

print "callback", w

print "deleting f"
del f
print "collecting"
gc.collect()
print "done"

print "callback", w

print "creating f"
f = Foo()
print "collecting"
gc.collect()
print "done"

print "callback", w

print "deleting f"
del f
print "collecting"
gc.collect()
print "done"

print "callback", w

print "creating f
