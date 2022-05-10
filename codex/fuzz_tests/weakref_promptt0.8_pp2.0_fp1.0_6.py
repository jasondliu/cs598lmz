import weakref
# Test weakref.ref and weakref.ProxyType

import sys
import copy
import cPickle
import weakref
from test import test_support

class C(object):
    pass

def check(ref, expected):
    if ref() is not expected:
        raise RuntimeError("expected %r, got %r" % (expected, ref()))

def check_dead(ref):
    try:
        ref()
    except ReferenceError:
        pass
    else:
        raise RuntimeError("expected ReferenceError")

def get_id(obj):
    return id(obj)

class ProxyTest(object):
    def test_basic(self):
        C.__module__ = "weakref_test"
        c = C()
        r = self.ref(c)
        x = r()
        if x is not c:
            raise RuntimeError("expected c, got %r" % (x,))

    def test_call(self):
        C.__module__ = "weakref_test"
        c = C()
        r = self.ref(c)
        if
