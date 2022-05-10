import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without a callback
class A:
    pass
a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect()

# Test gc.collect() with a callback
def callback():
    print "callback"
class A:
    pass
a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect(callback)

# Test gc.collect() with a callback that raises an exception
def callback():
    print "callback"
    raise ValueError
class A:
    pass
a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect(callback)

# Test gc.collect() with a callback that raises an exception
# and a weakref
def callback():
    print "callback"
    raise ValueError
class A:
    pass
a = A()
b = A()
a.b = b
b.a = a
wr = weakref.ref(
