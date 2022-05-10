import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() sometimes does collect weakrefable objects
# Note: gc.collect is a different function when gc is running
# under pypy, so this test is skipped.
if '__pypy__' not in sys.builtin_module_names:
    assert gc.collect() == 0
    class A:
        pass
    ra = weakref.ref(A())
    assert gc.collect() == 1
