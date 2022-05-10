import _struct
# Test _struct.Struct
import sys
import unittest
from test import test_support
import warnings

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('hHiIlLqQfd')
        self.assertEqual(s.size, 42)
