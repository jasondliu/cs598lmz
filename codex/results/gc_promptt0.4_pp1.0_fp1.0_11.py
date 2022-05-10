import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback that raises an exception.
# The exception should not prevent collection of the object.

class C:
    pass

def callback(wr):
    raise Exception

c = C()
wr = weakref.ref(c, callback)

del c
gc.collect()

print wr() is None
# Test gc.collect() with a weakref callback that raises an exception.
# The exception should not prevent collection of the object.

class C:
    pass

def callback(wr):
    raise Exception

c = C()
wr = weakref.ref(c, callback)

del c
gc.collect()

print wr() is None
# Test gc.collect() with a weakref callback that raises an exception.
# The exception should not prevent collection of the object.

class C:
    pass

def callback(wr):
    raise Exception

c = C()
wr = weakref.ref(c, callback)

del c
gc.collect()

print wr() is None
# Test gc.collect() with a weakref callback
