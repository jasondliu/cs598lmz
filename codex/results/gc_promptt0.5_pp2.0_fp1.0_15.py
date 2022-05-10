import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    global x
    x = []
    x.append(x)
    gc.collect()

f()
del x
gc.collect()

# Test gc.disable()
gc.disable()
def f():
    global x
    x = []
    x.append(x)
    gc.collect()

f()
del x
gc.collect()
gc.enable()

# Test gc.isenabled()
gc.isenabled()
gc.disable()
gc.isenabled()
gc.enable()
gc.isenabled()

# Test gc.get_threshold()
gc.get_threshold()

# Test gc.set_threshold()
gc.set_threshold(1, 2, 3)
gc.get_threshold()
gc.set_threshold(10, 20, 30)
gc.get_threshold()

# Test gc.get_count()
gc.get_count()

# Test gc.set_debug()
gc.set_debug(gc.DEBUG_ST
