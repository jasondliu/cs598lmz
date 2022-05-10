import weakref
# Test weakref.ref, weakref.proxy, weakref.ProxyTypes
import unittest
import gc
import random
import sys
import pickle
import repr
import copy
from test import test_support
import operator


class C:
    def __init__(self, arg=None):
        self.arg = arg

    def __cmp__(self, other):
        if type(other) == type(0):
            return cmp(self.arg, other)
        return cmp(id(self), id(other))

    def __repr__(self):
        return str(id(self))

    def __hash__(self):
        return hash(self.arg)

    def __call__(self, *args, **kwargs):
        return "__call__: %r %r" % (args, kwargs)

    def method(self, arg):
        return "method: %r" % arg


class D(C):
    pass


class TestBase:

    def test_basic(self):
        o = C(1)
