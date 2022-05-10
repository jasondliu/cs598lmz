import _struct
# Test _struct.Struct with single format character
from test import support
import unittest
from io import StringIO

# This test is used to make sure that the test suite does not rely on the
# struct module to be "complete"

class _StructTest(unittest.TestCase):
    def test_struct(self):
        self.assertEqual(_struct.Struct('x').unpack(b'x'),
                         (b'x',))
        self.assertEqual(_struct.Struct('x').pack(*(b'x',)), b'x')

class _StructTest(unittest.TestCase):
    def test_struct(self):
        self.assertEqual(_struct.Struct('x').unpack(b'x'),
                         (b'x',))
        self.assertEqual(_struct.Struct('x').pack(*(b'x',)), b'x')

class _StructTest(unittest.TestCase):
    def test_struct(self):
        self.assertEqual(_struct.Struct('x').unpack(b'x'),
                         (b'x',))
