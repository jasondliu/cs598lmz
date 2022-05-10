import codecs
# Test codecs.register_error.

import codecs
import unittest

from test import support

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error()

        # Test a simple replacement handler
        def replace1(exc):
            if isinstance(exc, UnicodeDecodeError):
                return ('x', exc.end)
            else:
                raise TypeError("don't know how to handle %r" % exc)
        codecs.register_error("test.replace1", replace1)

        self.assertEqual(codecs.strict_errors, "strict")
        codecs.register_error("test.strict", codecs.strict_errors)
        self.assertEqual(codecs.strict_errors, "test.strict")
        codecs.register_error("test.replace1", codecs.strict_errors)
        self.assertEqual(codecs.strict_errors, "test.replace1")

        for errors in ("test.replace1", "test
