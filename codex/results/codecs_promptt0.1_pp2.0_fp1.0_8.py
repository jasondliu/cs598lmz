import codecs
# Test codecs.register_error()

import codecs
import unittest

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Test registering an error handler
        def ignore_errors(exc):
            if isinstance(exc, UnicodeDecodeError):
                return (u'', exc.end)
            raise TypeError("don't know how to handle %r" % exc)
        codecs.register_error("ignore", ignore_errors)
        self.assertEqual(codecs.lookup_error("ignore"), ignore_errors)
        self.assertEqual(codecs.strict_errors(UnicodeDecodeError(
            "ascii", "\xff", 0, 1, "ouch")),
            (u'\ufffd', 1))
        self.assertEqual(codecs.ignore_errors(UnicodeDecodeError(
            "ascii", "\xff", 0, 1, "ouch")),
            (u'', 1))
        self.assertRaises(TypeError, codecs.ignore_errors, Look
