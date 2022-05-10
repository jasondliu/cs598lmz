import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

class A:
    pass

class B:
    pass

def callback(wr):
    print "callback called"

a = A()
b = B()
a.b = b
b.a = a

wr = weakref.ref(a, callback)
del a
del b
gc.collect()
print wr()

# Test gc.collect() with a weakref callback that raises an exception.

class A:
    pass

class B:
    pass

def callback(wr):
    print "callback called"
    raise ValueError

a = A()
b = B()
a.b = b
b.a = a

wr = weakref.ref(a, callback)
del a
del b
gc.collect()
print wr()

# Test gc.collect() with a weakref callback that raises an exception
# and a weakref that has a finalizer.

class A:
    pass

class B:
    pass

def callback(wr):
    print "callback called"
   
