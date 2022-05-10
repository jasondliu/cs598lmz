import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []
for i in range(10):
    a.append(weakref.ref(a))
    b = a[:]
    del b
    #print gc.collect()
    print gc.collect()

# Test gc.garbage
a = []
for i in range(10):
    a.append(weakref.ref(a))
    b = a[:]
    del b
    #print gc.collect()
    print gc.garbage

# Test gc.get_objects()
a = []
for i in range(10):
    a.append(weakref.ref(a))
    b = a[:]
    del b
    #print gc.collect()
    print gc.get_objects()

# Test gc.get_referrers()
a = []
for i in range(10):
    a.append(weakref.ref(a))
    b = a[:]
    del b
    #print gc.collect()
    print gc.get_referrers(a)

