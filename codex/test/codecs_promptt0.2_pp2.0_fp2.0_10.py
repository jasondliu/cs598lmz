import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def handler(exception):
            return (u"", exception.end)
        codecs.register_error("test.ignore", handler)
        self.assertEqual(codecs.lookup_error("test.ignore"), handler)
        self.assertRaises(LookupError, codecs.lookup_error, "test.ignore2")
        self.assertRaises(TypeError, codecs.register_error, "test.ignore",
                          lambda x, y: (u"", y))
        self.assertRaises(TypeError, codecs.register_error, "test.ignore",
                          lambda x: (u"", x))
        self.assertRaises(TypeError, codecs.register_error, "test.ignore",
                          lambda x: (u"", x, x))
