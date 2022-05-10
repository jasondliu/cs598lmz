import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() by making a list of weak references to the
# objects in a list.
def test_collect():
    # Create a list of weak references to the objects in a list.
    def make_list():
        objects = [C(), C()]
        refs = [ weakref.ref(obj) for obj in objects ]
        del objects
        return refs
    # Keep creating lists of weak references to objects
    # until one of the weak references has been collected.
    refs = make_list()
    while 1:
        gc.collect()
        if refs[0]() is None:
            break
        refs = make_list()
# Run the test.
test_collect()

# Check the garbage collector's debug flags.
print "gc.get_debug()", gc.get_debug()
# Turn on the garbage collector's debug flags.
gc.set_debug(gc.DEBUG_STATS)
# Run the test again.
test_collect()
# Check the garbage collector's debug flags again.
print "gc.get_debug()", gc.get_debug
