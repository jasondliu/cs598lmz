import weakref
# Test weakref.ref(x)
# Test weakref.proxy(x)
# Test weakref.getweakrefcount(x)
# Test weakref.getweakrefs(x)
# Test weakref.WeakKeyDictionary
# Test weakref.WeakValueDictionary
# Test weakref.WeakSet
# Test weakref.finalize
# Test weakref.ReferenceType
# Test weakref.CallableProxyType
# Test weakref.ProxyType
# Test weakref.ProxyTypes
# Test weakref.ProxyTypes + _testcapi

import unittest
import io
import sys
import threading
import gc
import contextlib
import pickle
import copy
import test.support
import test.support as support
from test.support.script_helper import assert_python_ok
from test.support import import_module

class BasicTest:
    def test_basic(self):
        # Create a cycle
        l = []
        l.append(l)
        # Create a weak reference to the cycle
        p = self.proxy(l)
        # Enter the reference into a dictionary
       
