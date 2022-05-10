import codecs
# Test codecs.register_error
# See http://bugs.python.org/issue8104

import codecs
import unittest
import tempfile
import os
import sys

class TestCodecs(unittest.TestCase):

    def test_register_error(self):
        # The default codecs.strict_errors raises a UnicodeDecodeError
        self.assertRaises(UnicodeDecodeError, codecs.decode, b"\xff", "ascii")
        # Registering a new error handler can change that
        def ignore_errors(exc):
            if isinstance(exc, UnicodeDecodeError):
                return (u"\ufffd", exc.end)
            raise TypeError("don't know how to handle %r" % exc)
        codecs.register_error("ignore", ignore_errors)
        self.assertEqual(codecs.decode(b"\xff", "ascii", "ignore"), u"\ufffd")
        # Check that the error handler is used for lookups, too
        self.assertEqual(codecs.lookup_error
