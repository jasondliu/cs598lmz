import _struct
# Test _struct.Struct
import unittest
import sys
import struct
import io
import copy
import pickle
import test.support
from test.support import bigaddrspacetest
from test import support
import _testcapi

if sys.version_info[:2] == (2, 6):
    # Skip this test on Python 2.6.
    raise unittest.SkipTest("test not appropriate for Python 2.6")

# Test _struct.Struct

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        # check _struct.Struct
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct(42)
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct('', 42)
        with self.assertRaises(TypeError):
            _struct.Struct('', '')
        with self.assertRaises(TypeError):
            _
