import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with None object.
class A(object):
    def __init__(self):
        self.x = 5
t=A()
id(t)

id(1)
 
id(None)

gc.collect()
gc.get_referrers(None)

wr = weakref.ref(t)
print wr()
print wr() is None

del t
gc.collect()
print wr()

wr = weakref.ref(None)
gc.collect()
 
gc.get_referrers(None)
import sys
sys.getrefcount(None)
import gc
class A(object):
    def __init__(self):
        self.x = 5
t=A()
gc.collect()
gc.get_referrers(None)
gc.get_referrers(t)

 
gc.collect()
 
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()

from sys import getrefcount
from six.moves import xrange
x =
