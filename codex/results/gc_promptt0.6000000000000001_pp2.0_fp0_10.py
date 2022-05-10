import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to an object.

class X:
    pass

x = X()
w = weakref.ref(x)

del x
gc.collect()

print(w)
# Test gc.collect() with a weakref to an object.

class X:
    pass

x = X()
w = weakref.ref(x)

del x
gc.collect()

print(w)
# Test gc.collect() with a weakref to an object in a container.

class X:
    pass

x = X()
w = weakref.ref(x)

l = [x]

del x
gc.collect()

print(w)
# Test gc.collect() with a weakref to an object in a container.

class X:
    pass

x = X()
w = weakref.ref(x)

l = [x]

del x
gc.collect()

print(w)
# Test gc.collect() with a weakref to an object in a container.

class
