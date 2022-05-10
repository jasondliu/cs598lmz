import weakref
# Test weakref.ref(obj, callback)
#
# The callback should be called when obj is garbage-collected.
#
# This test builds a cycle.

from test import support
from test.support import gc_collect


class X:
    pass

def callback(r):
    global obj, x, t
    obj = None
    x = None
    t = None

obj = X()
x = weakref.ref(obj, callback)
t = (x, obj)

gc_collect()
del obj, x, t
gc_collect()

support.gc_collect()

if support.verbose:
    print('All OK.')
