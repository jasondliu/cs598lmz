import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a weakref and a callback.
class C:
    pass
def callback(wr):
    print('callback!')
# Create a reference cycle.
c = C()
d = C()
c.foo = d
d.foo = c
w = weakref.ref(c, callback)
c = d = None
gc.collect()

# Test gc.collect with a weakref and no callback.
class C:
    pass
def callback(wr):
    print('callback!')
# Create a reference cycle.
c = C()
d = C()
c.foo = d
d.foo = c
w = weakref.ref(c)
c = d = None
gc.collect()

# This used to be a test for stack overflow in gc.  It no longer is.
#
# Loop the gc through lots of cycles, so it can free the cycles one
# at a time.
def my_callback(ignore):
    global c
    c = None
    gc.collect()
class C:
    pass
c = C()
c.foo =
