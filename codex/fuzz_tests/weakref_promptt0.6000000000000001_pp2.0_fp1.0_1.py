import weakref
# Test weakref.ref() on built-in types.
# This used to crash in 2.2.2, because the weakref destructor would
# decref the object's type, and the type then would be destroyed while
# still in use.
#
# The bug only occurred on 64-bit platforms with debug builds.
import sys
import gc
import weakref
import operator
import unittest
import test.test_support
import types

if not hasattr(sys, 'gettotalrefcount'):
    raise unittest.SkipTest('requires sys.gettotalrefcount()')

# Create a bunch of objects, some of which have __del__ methods.
# Keep them all in a list so they don't get garbage collected.
objects = []

class C(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'deleting', self

class D(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print 'deleting', self
