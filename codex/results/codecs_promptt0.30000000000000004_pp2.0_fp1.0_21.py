import codecs
# Test codecs.register_error()

import codecs
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        def g(exc):
            return (u"", exc.end)
        codecs.register_error("test.g", g)
        self.assertEqual(codecs.lookup_error("test.g"), g)
        self.assertRaises(LookupError, codecs.lookup_error, "test.h")
        codecs.register_error("test.h", g)
        self.assertEqual(codecs.lookup_error("test.h"), g)
        self.assertRaises(TypeError, codecs.register_error, "test.i", None)
        self.assertRaises(TypeError, codecs.register_error, "test.i", 42)
        self.assertRaises(TypeError, codecs.register_error, "test.i", "foo")
        self.assertRaises(TypeError, codecs.register_error, "test.i", ())
