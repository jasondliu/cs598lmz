import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref.finalize objects that
# run at exit.  It should be safe to collect them
# between when they are created and when they run.
#
# Previously, this would assert if a weakref.finalize
# object was collected before it was run.

class C:
    pass

def print_finalized(obj):
    print('C object finalized')

def test():
    obj = C()
    f = weakref.finalize(obj, print_finalized, 'extra argument')
    gc.collect()

test()
