import codecs
# Test codecs.register_error('ignore')
import os
import sys
import unittest
import warnings

from test import support
from test.support import TESTFN, run_unittest, unlink

class Error(Exception):
    pass

class CodecTest(unittest.TestCase):
    def test_register_error(self):
        # Testing the register_error function and error handling mechanism
        # This currently only tests the lookups in the error registry,
        # not the raising of the exceptions or the storing of the
        # replacements.
        #
        # This test is a bit contrived and doesn't really test the
        # error handling mechanism directly, but it is better than
        # nothing.

        # First test a simple error handler
        def simplehandler(exception):
            return 42, exception.end

        # Register this error handler under a new name
        codecs.register_error("test.simplehandler", simplehandler)

        # Now try to look up this error handler by name
        res = codecs.lookup_error("test.simplehandler")
        self.assertEqual(res, simplehandler)
