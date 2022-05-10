import weakref
# Test weakref.ref callbacks.
#
# Note:  See the standard library documentation for details on the semantics
# of weak references and callbacks.
#
# This test verifies the basic behavior, but not the thread-safety of callbacks.
#
# Mark Hammond's win32all package provided the inspiration for the
# basic approach taken here.
#

import unittest
from test import support

def foo(x):
    raise TypeError(x)

class Foo:
    def __init__(self):
        self.x = 1
    def __del__(self):
        self.x = 2

class MyException(Exception):
    pass

def mycallback(*args, **kw):
    raise MyException(args)


class CallbackRefTests(unittest.TestCase):
    def test_ref(self):
        obj = Foo()
        callback = self.callback = obj.__del__
        # Create a reference to obj which can trigger the callback on
        # object deletion, or when obj is assigned to a different value.
        ref = weakref.ref(obj, callback
