import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()  # force collection
gc.collect()  # collect again
def f():
    l = [object()] * 10
    return l

def g():
    l = f()
    l = None
    gc.collect()
    return l

l = g()
print(l)

# check that list is now collectable
gc.collect()

# check that list is not tracked anymore
l = g()
print(l)

# check that list is not tracked anymore
gc.collect()
print(gc.garbage)

# check that list is not tracked anymore
gc.collect()
print(gc.garbage)

# check that list is not tracked anymore
l = g()
print(l)

# check that list is not tracked anymore
gc.collect()
print(gc.garbage)

# check that list is now collectable
gc.collect()
print(gc.garbage)

del l
gc.collect()

# check that list is not tracked anymore
l = g()
print(l)

# check
