import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and weakref.finalize

# Before calling gc.collect, create a weakref to an object and register a
# finalizer for the weakref.  If the object is collected, the finalizer
# should be run.  We use the fact that the finalizer prints a message to
# verify that it was called.

# This test is a bit fragile because it depends on gc.collect() calling the
# finalizer.  It would be better to move the test to gc.py.

import gc, weakref

class Dummy:
    pass

def finalize(*args):
    print 'finalizing:', args

def test_finalize():
    dummy = Dummy()
    dummy.attr = dummy
    wr = weakref.ref(dummy, finalize)
    gc.collect()
    print 'expect 1 message:'
    del dummy
    gc.collect()
    print 'expect no messages:'
    print 'end'

test_finalize()
