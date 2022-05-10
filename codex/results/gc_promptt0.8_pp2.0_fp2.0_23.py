import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
l = []
for i in range(10):
    l.append(weakref.ref(gc.collect()))
    l[i]()

# Test gc.DEBUG_SAVEALL
gc.set_debug(gc.DEBUG_SAVEALL)
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()
gc.set_debug(0)

# Test finalize()
d = {}
ref = weakref.WeakKeyDictionary()
def check(ignored, d=d, ref=ref):
    for o in gc.garbage:
        if id(o) in d:
            return
        d[id(o)] = 1
        o.x = 1
    if len(gc.garbage) < 100:
        return
    del d[id(ref)]
    import gc
    gc.garbage.append(ref)
    gc.collect()
    raise SystemError
finalize = weakref.finalize(42, check)

def callback(ignore):
    raise System
