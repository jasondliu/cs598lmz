import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect seeds

def weak_refs(o):
    import gc
    r = []
    for i in range(1000):
        r.append(weakref.ref(o))
    prev = r[:]
    for r1 in r:
        for r2 in prev:
            if r1() is r2():
                return False
        prev.remove(r1)
        gc.collect()
        if r1() is None:
            return False
    return True

a = []
a1 = a
del a
if weak_refs(a1):
    print('weak ref test - OK')
else:
    print('weak ref test - FAILED')

a2 = weakref.ref(a1)
a1 = None
gc.collect()
if a2() is None:
    print('ref to soft gone obj - OK')
else:
    print('ref to soft gone obj - FAILED')

a3 = weakref.ref(a1)
gc.collect()
if a3() is None:
    print('ref to soft dead
