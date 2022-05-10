import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

class A:
    pass

class B:
    pass

def callback(wr):
    print("callback", wr)

a = A()
b = B()
a.b = b
b.a = a

# Create a weakref to a, but don't keep a reference to it
weakref.ref(a, callback)

# Create a weakref to b, but don't keep a reference to it
weakref.ref(b, callback)

# Create a weakref to a, but don't keep a reference to it
weakref.ref(a, callback)

# Create a weakref to b, but don't keep a reference to it
weakref.ref(b, callback)

# Create a weakref to a, but don't keep a reference to it
weakref.ref(a, callback)

# Create a weakref to b, but don't keep a reference to it
weakref.ref(b, callback)

# Create a weakref to a, but don't keep a reference to it
weakref.ref(a, callback
