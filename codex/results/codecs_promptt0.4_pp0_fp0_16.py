import codecs
# Test codecs.register_error

import codecs
import unittest

from test import support

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        def handler(exc):
            return (u"\ufffd", exc.end)
        codecs.register_error("test.register_error", handler)
        self.assertEqual(codecs.lookup_error("test.register_error"), handler)
        self.assertEqual(codecs.lookup_error("test.register_error"),
                         codecs.lookup_error("test.register_error"))
        self.assertNotEqual(codecs.lookup_error("test.register_error"),
                            codecs.lookup_error("test.register_error2"))
        self.assertNotEqual(codecs.lookup_error("test.register_error"),
                            codecs.lookup_error("xmlcharrefreplace"))
        self.assertEqual(codecs.strict_errors,
                         codecs.lookup_error("strict"))
