import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a list of objects that are not referenced anywhere
# except in the list.

class Test:
    pass

def f():
    l = []
    for i in range(10):
        o = Test()
        l.append(o)
    gc.collect()
    print len(gc.garbage)

f()
