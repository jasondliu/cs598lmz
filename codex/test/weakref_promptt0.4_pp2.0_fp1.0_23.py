import weakref
# Test weakref.ref() and weakref.proxy()
import weakref as wr

import gc
import operator
import sys
import unittest

from test import support

# Base class for testing weak references.

class ReferenceTest:
    thetype = None

    def setUp(self):
        self.objects = []
        self.refs = []
        self.proxies = []
        self.target = object()
        self.objects.append(self.target)

    def tearDown(self):
        del self.objects[:]
        del self.refs[:]
        del self.proxies[:]

    def make_object(self, key=None):
        obj = object()
        self.objects.append(obj)
        self.refs.append(self.thetype(obj, key))
        return obj

    def make_proxy(self, key=None):
        obj = object()
        self.objects.append(obj)
        self.proxies.append(self.thetype(obj, key))
        return obj

