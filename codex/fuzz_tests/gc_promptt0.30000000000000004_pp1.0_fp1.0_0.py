import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref.ref()
r = weakref.ref(C(1))
gc.collect()

# Test weakref.proxy()
p = weakref.proxy(C(2))
gc.collect()

# Test weakref.getweakrefcount()
w = weakref.ref(C(3))
gc.collect()

# Test weakref.getweakrefs()
w = weakref.ref(C(4))
gc.collect()

# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
d[C(5)] = 6
gc.collect()

# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
d[6] = C(7)
gc.collect()

# Test weakref.finalize
def callback(x):
    print("finalized", x)

def make_callback(x):
    return lambda: callback(x)

finalizer = weakref.finalize(C(8), make_callback(8))
gc.
