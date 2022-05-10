import codecs
# Test codecs.register_error.
import string
import sys
import test_support
import unittest

class Test_register_error(unittest.TestCase):

    def test_register_error(self):
        # Make sure we have a lookup function
        def lookup(errors):
            return codecs.replace_errors
        codecs.register_error("test.lookup", lookup)
        # Make sure we have a replace function
        def replace(exc):
            if not isinstance(exc, UnicodeDecodeError):
                raise TypeError("don't know how to handle %r" % exc)
            return u"\ufffd", exc.end
        codecs.register_error("test.replace", replace)

        # Encode a string with a bad char
        s = u"abc\u1111def"
        self.assertEqual(s.encode("ascii", "test.replace"), "abc\ufffddef")
        self.assertEqual(s.encode("ascii", "test.lookup"), "abc\ufffddef")
        self.assertRaises(Type
