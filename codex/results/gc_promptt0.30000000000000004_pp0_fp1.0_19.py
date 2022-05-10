import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

class A:
    pass

class B:
    pass

def callback(w):
    print "callback"

a = A()
b = B()
a.b = b
b.a = a

w = weakref.ref(a, callback)

print "collecting"
gc.collect()
print "done"

del a
print "collecting"
gc.collect()
print "done"

# Test gc.collect() with a weakref callback that raises an exception

class A:
    pass

class B:
    pass

def callback(w):
    print "callback"
    raise ValueError

a = A()
b = B()
a.b = b
b.a = a

w = weakref.ref(a, callback)

print "collecting"
gc.collect()
print "done"

del a
print "collecting"
gc.collect()
print "done"

# Test gc.collect() with a weakref callback that raises an exception
# and a
