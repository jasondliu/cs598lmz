import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
#
# This test is not exhaustive, but it does test the basic functionality.
#
# We run the tests twice to make sure that the garbage collector is
# working correctly even if some objects survive until the second
# collection.
#
# We also run the tests with and without the garbage collector enabled,
# to make sure that doesn't make a difference.

import weakref
import gc

class C(object):
    pass

class D(C):
    pass

class E(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        del self.x

class F(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        self.x = None

class G(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        self.x = C()

class H(object):
    def __init__(self, x):
        self.x
