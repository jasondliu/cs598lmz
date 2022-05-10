import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

class A:
    pass

def callback(wr):
    print "callback called"

a = A()
wr = weakref.ref(a, callback)

print "collecting"
gc.collect()
print "done"

print "collecting"
del a
gc.collect()
print "done"

# Test gc.collect() with a weakref callback

class A:
    pass

def callback(wr):
    print "callback called"

a = A()
wr = weakref.ref(a, callback)

print "collecting"
gc.collect()
print "done"

print "collecting"
del a
gc.collect()
print "done"

# Test gc.collect() with a weakref callback

class A:
    pass

def callback(wr):
    print "callback called"

a = A()
wr = weakref.ref(a, callback)

print "collecting"
gc.collect()
print "done"

print "collecting"
del a
