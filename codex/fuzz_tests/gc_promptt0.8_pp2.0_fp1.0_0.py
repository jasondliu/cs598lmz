import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

# create cyclic object structure

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a

# create weakref

w = weakref.ref(b)


# delete a

del a

# The weakref to b is still alive. The gc module
# doesn't currently know about weakrefs, but it is
# aware of the fact that b has a reference to a, that
# is dead. gc.collect() will therefore collect a,
# and since there are no other references to it,
# the obect is not resurrected.

gc.collect()

b.attr = 1

if w() is b:
    print "weakref still pointing to b"
else:
    raise TestFailed, "weakref not pointing to b"

# Try some other tests.

globals()['b'] = b
globals()['w'] = w

del b, w
gc.collect()

if globals()['w']() is globals()
