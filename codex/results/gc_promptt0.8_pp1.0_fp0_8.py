import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with callback
class C:
    pass

def callback(ignored):
    global callback_called
    callback_called = True

callback_called = False

# Make an object and delete it.
C()
gc.collect()
assert not callback_called

# Make an object, delete it, collect it.
# gc.DEBUG_COLLECTABLE makes sure it isn't unlinked.
x = C()
del x
gc.collect()
assert callback_called
callback_called = False

# Make an object and collect it.
C()
gc.collect()
assert callback_called
callback_called = False

# Make an object, delete it, collect it, add a callback.
x = C()
del x
gc.collect()
assert callback_called
callback_called = False
gc.callbacks.append(callback)
gc.collect()
assert callback_called
callback_called = False
gc.callbacks.remove(callback)

gc.collect()
assert not callback_called

# Make an object, add a callback, collect it.
x = C()
gc
