import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegister(unittest.TestCase):
    def test_register(self):
        def my_replace(exc):
            return (u'', exc.start + 1)
        codecs.register_error("test.my_replace", my_replace)
        self.assertRaises(LookupError, codecs.register_error, "test.my_replace", my_replace)
        self.assertRaises(TypeError, codecs.register_error, "test.my_replace", None)
        self.assertRaises(TypeError, codecs.register_error, "test.my_replace", "replace")
        self.assertRaises(TypeError, codecs.register_error, "test.my_replace", "")
        self.assertRaises(TypeError, codecs.register_error, "test.my_replace", "strict")
        self.assertRaises(TypeError, codecs.register_error, "test.my_replace", "ignore")
