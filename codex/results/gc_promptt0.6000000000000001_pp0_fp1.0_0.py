import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
# Test weakref
a=[]
b=[]
for i in range(10):
    a.append(weakref.ref(i))
    b.append(i)
del b
gc.collect()
for i in a:
    print(i())
del a
gc.collect()
# Test weakref callbacks
class A:
    pass
def callback(x):
    print("callback", x)
a=A()
ref=weakref.ref(a, callback)
del a
gc.collect()

# Test cyclic gc
# This is a bit of a nasty test for gc, since it uses a lot of memory.
# It does not test much of the gc module; mostly it just checks that
# it doesn't crash.

# The test is designed to create a cyclic garbage object with a size
# of a megabyte.  Since the object is inaccessible, it should be
# garbage collected.  On many systems, the object will be split into
# multiple objects.  On some, it may not be.


