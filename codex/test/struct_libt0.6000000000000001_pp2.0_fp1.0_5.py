import _struct
import sys
import types
import unittest

from test import support
from test.support import import_helper


class StructTest(unittest.TestCase):

    def test_error_attributes(self):
        # Test that the correct exception and error message are raised
        # when the struct module is given bad input.
        try:
            _struct.error
        except AttributeError as msg:
            self.fail("module struct has no attribute 'error': %s" % msg)

        try:
            struct.error
        except AttributeError as msg:
            self.fail("module struct has no attribute 'error': %s" % msg)

        e = struct.error
        self.assertEqual(e.__class__, type(e))
        self.assertEqual(e.__class__.__name__, "error")
        self.assertEqual(e.__class__.__module__, "struct")
        self.assertEqual(e.__doc__, "unpack requires a bytes object of length 4")

