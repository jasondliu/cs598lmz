import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Testing codecs.register_error()
        def handler(exception):
            return (u"\ufffd", exception.end)
        codecs.register_error("test.xmlcharrefreplace", handler)
        self.assertEqual(codecs.lookup_error("test.xmlcharrefreplace"), handler)
        self.assertEqual(codecs.lookup_error("test.xmlcharrefreplace"), handler)
        self.assertRaises(LookupError, codecs.lookup_error, "test.undefined")

        # Testing codecs.lookup_error()
        self.assertEqual(codecs.lookup_error("strict"), codecs.strict_errors)
        self.assertEqual(codecs.lookup_error("ignore"), codecs.ignore_errors)
