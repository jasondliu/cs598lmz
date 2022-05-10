import codecs
# Test codecs.register_error
import re
import sys
import unittest
import weakref
import warnings
from test import support
from test.support.script_helper import assert_python_ok, assert_python_failure, assert_python_warns, assert_python_failure, assert_python_ok, assert_python_warns

class TestUnicode(unittest.TestCase):
    """Test the Unicode implementation."""

    def test_constructor(self):
        u = unicode()
        self.assertEqual(u, '')
        self.assertEqual(len(u), 0)
        self.assertNotIn(u, ('\x00', '\0', '0', 0, ''))
        u = unicode('abc')
        self.assertEqual(u, 'abc')
        self.assertEqual(len(u), 3)
        self.assertNotIn(u, ('\x00', '\0', '0', 0, '', 'abc'))
        u = unicode('abc', 'ascii')
        self.assertEqual(u
