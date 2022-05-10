import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []
b = []
a.append(b)
a.append(b)
a.append(b)
a.append(b)
a.append(b)
del a
del b
gc.collect()
# Test gc.get_referrers()
# Test gc.get_referents()
# Test gc.get_objects()
# Test gc.get_count()
def f():
    a = []
    a.append(a)
    return a

a = f()
gc.collect()
del f
gc.collect()
# Test gc.get_threshold()
# Test gc.set_threshold()
# Test gc.enable()
# Test gc.disable()
# Test gc.isenabled()
# Test gc.set_debug()
# Test gc.get_debug()
# Test gc.set_debug()
# Test gc.set_debug()
# Test gc.set_debug()
# Test gc.set_debug()
# Test gc.set_debug
