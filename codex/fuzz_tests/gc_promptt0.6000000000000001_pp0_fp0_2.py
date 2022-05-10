import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref callback.
# A callback is called when the referent is collected.

class C:
    pass

def callback(wr):
    print('callback', wr)
    print('    callback: wr.ref is', wr.ref)
    print('    callback: wr.obj is', wr.obj)
    print('    callback: wr() is', wr())

# Case 1: object is not collected
print('Case 1: object is not collected')
obj = C()
wr = weakref.ref(obj, callback)
del obj
gc.collect()
print(wr.ref)
print(wr.obj)
print(wr())

# Case 2: object is collected
print('\nCase 2: object is collected')
obj = C()
wr = weakref.ref(obj, callback)
del obj
gc.collect()
print(wr.ref)
print(wr.obj)
print(wr())

# Case 3: object is collected, but the callback is cleared
print('\nCase 3: object is collected, but the callback is cleared')
obj = C()
