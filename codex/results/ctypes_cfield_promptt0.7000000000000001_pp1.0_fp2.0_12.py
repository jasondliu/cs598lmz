import ctypes
# Test ctypes.CField objects
import datetime
import decimal
import io
import math
import operator
import pickle
import random
import struct
import sys
import textwrap
import time
import unittest
import weakref
from collections import OrderedDict
from decimal import Decimal
from test import support
from test.support import TESTFN, run_unittest, check_impl_detail, \
    import_module
import builtins

# Work around http://bugs.python.org/issue9424
class FooBar(tuple): pass

# This class is used to make sure the destructor for the C object is called
# when the wrapper is destroyed, to avoid segfaults.
class CallbackTest:
    def __init__(self):
        self.called = False

    def callback(self):
        self.called = True

class _CDataTestBase(unittest.TestCase):
    # Subclasses must override
    type2test = None

    def test_create(self):
        x = self.type2test(42)
        self.assertEqual(x, 42)

   
