import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage.  If a test fails, it will print
# a message and return a false value.  If all tests succeed, it will
# return a true value.
def test_gc(verbose=None):
    if verbose is None:
        verbose = (__debug__ and sys.stdout or 0)
    if verbose:
        def show(msg):
            print(msg)
    else:
        def show(msg):
            pass
    ok = 1
    class C:
        pass
    old_objects = len(gc.get_objects())
    gc.collect()
    new_objects = len(gc.get_objects())
    if new_objects != old_objects:
        show("at start up, %d objects in system, not %d" %
             (new_objects, old_objects))
        ok = 0
    if gc.garbage:
        show("gc.garbage not empty at start up: " + str(gc.garbage))
        ok = 0
    class C(object):
        pass
    c
