import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        def handler(exception):
            return (u"", exception.end)
        codecs.register_error("test.strict", handler)
        self.assertEqual(codecs.lookup_error("test.strict"), handler)
        self.assertRaises(LookupError, codecs.lookup_error, "test.strict2")
        codecs.register_error("test.strict2", handler)
        self.assertEqual(codecs.lookup_error("test.strict2"), handler)
        self.assertRaises(TypeError, codecs.register_error, "test.strict3", "foo")
        self.assertRaises(TypeError, codecs.register_error, "test.strict4", handler, 42)
        self.assertRaises(TypeError, codecs.register_error, "test.strict5", handler, "foo")
        self.assert
