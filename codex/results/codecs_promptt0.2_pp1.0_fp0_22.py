import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test registering a new error handler
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.my_error', handler)
        self.assertEqual(codecs.lookup_error('test.my_error'), handler)

        # Test registering an existing error handler
        def handler2(exception):
            return (u'', exception.end)
        codecs.register_error('test.my_error', handler2)
        self.assertEqual(codecs.lookup_error('test.my_error'), handler2)

        # Test registering an error handler with a wrong type
        self.assertRaises(TypeError, codecs.register_error, 'test.my_error', 42)

        # Test registering an error handler with a wrong number of arguments
        def handler3(exception):
            return (u'', exception.end)
        self.
