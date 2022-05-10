import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Testing codecs.register_error
        def handler(exc):
            return (u"", exc.end)
        codecs.register_error("test.strict", handler)
        self.assertEqual(codecs.lookup_error("test.strict"), handler)
        self.assertRaises(LookupError, codecs.lookup_error, "test.unknown")
        self.assertRaises(TypeError, codecs.register_error, "test.strict", None)
        self.assertRaises(TypeError, codecs.register_error, "test.strict", "")
        self.assertRaises(TypeError, codecs.register_error, "test.strict", 42)
        self.assertRaises(TypeError, codecs.register_error, "test.strict", ())
        self.assertRaises(TypeError, codecs.register_error, "test.strict",
