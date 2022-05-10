import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test codecs.register_error
        def bad_handler(exception):
            raise TypeError("bad handler")
        def good_handler(exception):
            return (u"", exception.end)
        self.assertRaises(TypeError, codecs.register_error, bad_handler)
        codecs.register_error("test.bad_handler", bad_handler)
        self.assertRaises(TypeError, codecs.register_error, "test.bad_handler", bad_handler)
        codecs.register_error("test.good_handler", good_handler)
        codecs.register_error("test.good_handler", None)
        codecs.register_error("test.good_handler", good_handler)
        codecs.register_error("test.good_handler", None)
        codecs.register_error("test.good_handler", good_handler)
