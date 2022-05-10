import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage
a = []
a.append(a)
del a
gc.collect()
if len(gc.garbage) != 1:
    print "gc.garbage contains", len(gc.garbage), "items, should be 1"
if gc.garbage:
    print "gc.garbage[0] is", type(gc.garbage[0])
    if gc.garbage[0] is not gc.garbage[0]:
        print "gc.garbage[0] is not gc.garbage[0]"
    else:
        print "gc.garbage[0] is gc.garbage[0]"
    del gc.garbage[0]
    if gc.garbage:
        print "garbage not empty after deleting its only element"
# Test that the outermost container of a cyclic trash is always collectable
def check(obj):
    del obj
    gc.collect()
    if len(gc.garbage) != 1:
        print "object not in garbage"
    elif gc.
