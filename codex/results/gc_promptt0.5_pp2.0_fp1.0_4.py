import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.
#
# This test is intended to be run in a subprocess, so that the
# gc module can be tested without interference from other
# threads.  To run it in a subprocess, use the -m switch with
# the Python interpreter:
#
#   python -m test.regrtest -uall -x test_gc

import unittest
import gc
import weakref
import sys
import os
import gc
import re
import time

# Test weakref callbacks

class Foo(object):
    pass

class Foo2(object):
    def __del__(self):
        pass

class Foo3(object):
    def __del__(self):
        pass

class Foo4(object):
    def __init__(self):
        self.x = Foo()

class Foo5(object):
    def __init__(self):
        self.x = Foo2()

class Foo6(object):
    def __init__(self):
        self.x = Foo3()

class Foo7(object
