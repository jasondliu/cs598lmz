import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(w):
    print "callback"

f = Foo()
w = weakref.ref(f, callback)

print "before:", gc.collect()
print "after:", gc.collect()

del f
print "after:", gc.collect()

# Test gc.get_referrers()

class Foo:
    pass

f = Foo()

def callback(w):
    print "callback"

w = weakref.ref(f, callback)

print "before:", gc.collect()
print "after:", gc.collect()

del f
print "after:", gc.collect()

# Test gc.get_objects()

class Foo:
    pass

f = Foo()

def callback(w):
    print "callback"

w = weakref.ref(f, callback)

print "before:", gc.collect()
print "after:", gc.collect()

del f
print "after:", gc
