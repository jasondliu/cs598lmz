import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.
# This is a regression test for a bug that caused
# a crash when the callback tried to remove the
# weakref from the list of weakrefs to be called.
#
# The bug was introduced by a change to gcmodule.c
# on 2006-01-21.
#
# This test should be run with the -l option, to
# enable the display of the gc list.  It should
# show that the weakref callback is called, and
# that the weakref is removed from the list of
# weakrefs to be called.

import gc
gc.set_debug(gc.DEBUG_COLLECTABLE)

class C:
    pass

def callback(w):
    print 'callback'
    gc.collect()
    print 'end callback'

c = C()
w = weakref.ref(c, callback)
del c
gc.collect()
print 'end of test'
