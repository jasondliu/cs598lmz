import codecs
# Test codecs.register_error
from test import test_support
import unittest


class CodecsRegisterErrorTest(unittest.TestCase):
    def test_lookup_error(self):
        self.assertRaises(LookupError, codecs.lookup_error, "undefined")
        # to test defaulting logic
        self.assertRaises(LookupError, codecs.lookup_error, "undefined_abc")

    @unittest.skipUnless(codecs.lookup_error("strict"), "strict error handling required")
    def test_strict(self):
        self.assertEqual(codecs.lookup_error("strict"), codecs.lookup_error("strict_errors"))
        s = "spam"
        self.assertRaises(UnicodeDecodeError, s.decode, "ascii", "strict")
        self.assertRaises(UnicodeEncodeError, s.encode, "ascii", "strict")
        self.assertRaises(UnicodeError, s.translate, {
