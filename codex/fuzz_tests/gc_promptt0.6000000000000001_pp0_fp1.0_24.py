import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []
for i in range(10):
    a.append(weakref.ref(str(i)))
    gc.collect()
    b = str(i)
    a[-1]()
    gc.collect()
    del b
    gc.collect()

# Test gc.can_collect()
a = []
for i in range(10):
    a.append(weakref.ref(str(i)))
    assert gc.can_collect()
    b = str(i)
    assert gc.can_collect()
    a[-1]()
    assert gc.can_collect()
    del b
    assert gc.can_collect()

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
# Test gc.collect()
a = []
for i in range(10):
    a.append(weakref.ref(str(i)))
    gc.collect()
    b = str(i)
    a[-1]()
    gc.collect()
    del b
   
