import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

def callback(ignored):
    print('called back')

def f():
    o = object()
    r = weakref.ref(o, callback)
    print('created ref')
    del o
    print('deleted object')
    gc.collect()
    print('collected')

f()

print('done')

# Test gc.get_referrers()

def callback(ignored):
    print('called back')

def f():
    o = object()
    r = weakref.ref(o, callback)
    print(gc.get_referrers(r))
    print(gc.get_referrers(o))
    del o
    print('deleted object')
    gc.collect()
    print('collected')

f()

print('done')

# Test gc.get_objects()

def callback(ignored):
    print('called back')

def f():
    o = object()
    r = weakref.ref(o, callback)
    print(gc.
