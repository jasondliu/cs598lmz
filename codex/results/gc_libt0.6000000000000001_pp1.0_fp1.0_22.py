import gc, weakref, _weakref
from test.support import captured_stdout, run_unittest, TESTFN, unlink, \
    get_attribute, cpython_only, import_module
from test.support.script_helper import assert_python_ok
import sys
import unittest
from collections import Counter
import warnings
import pdb

# NOTE: _testcapi is not covered by the general test_api (see comment there)
import _testcapi

# Test weakref.proxy()

class MyClass:
    pass

class MySubclass(MyClass):
    pass

class TestWeakref(unittest.TestCase):

    def test_basic(self):
        o = MyClass()
        p = weakref.proxy(o)
        self.assertIs(type(p), weakref.ProxyType)
        self.assertIs(p.__class__, MyClass)
        self.assertIs(type(p), o.__class__)
        self.assertIs(type(p), type(o))
        self.assertEqual(p.__
