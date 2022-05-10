import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test the registration of error handlers
        #
        # First, register an error handler under a new name
        def ignore_errors(exc):
            if isinstance(exc, UnicodeEncodeError):
                return (u"ignore", exc.end)
            elif isinstance(exc, UnicodeDecodeError):
                return (u"ignore", exc.end)
            elif isinstance(exc, UnicodeTranslateError):
                return (u"ignore", exc.end)
            else:
                raise TypeError("don't know how to handle %r" % exc)
        codecs.register_error("ignore", ignore_errors)
        # Encode and decode a string with 'ignore'
        self.assertEqual(u"abc".encode("ascii", "ignore"), "abc")
        self.assertEqual(u"\u1234".encode("ascii", "ignore"), "")
        self.assertE
