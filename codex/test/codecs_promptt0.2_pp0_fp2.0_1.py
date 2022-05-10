import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test registering an error handler
        def handler(exception):
            return (u"", exception.end)
        codecs.register_error("test.lookup", handler)
        self.assertEqual(codecs.lookup_error("test.lookup"), handler)
        # Test registering an error handler with a name
        def handler(exception):
            return (u"", exception.end)
        codecs.register_error("test.lookup2", handler, "test.lookup2")
        self.assertEqual(codecs.lookup_error("test.lookup2"), handler)
        # Test registering an error handler with a name and docstring
        def handler(exception):
            return (u"", exception.end)
        codecs.register_error("test.lookup3", handler, "test.lookup3",
                              "docstring")
