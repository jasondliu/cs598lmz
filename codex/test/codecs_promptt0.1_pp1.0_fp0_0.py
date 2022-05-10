import codecs
# Test codecs.register_error

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Test registering an error handler
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.myerrorhandler', handler)
        self.assertEqual(codecs.lookup_error('test.myerrorhandler'), handler)
        self.assertRaises(LookupError, codecs.lookup_error, 'test.nosuchhandler')

        # Test registering an error handler with a name that already exists
        def handler(exception):
            return (u'', exception.end)
        self.assertRaises(TypeError, codecs.register_error, 'test.myerrorhandler', handler)

        # Test registering an error handler with a name that is not a string
        def handler(exception):
            return (u'', exception.end)
        self.assertRaises(TypeError, codecs.register_error, 42, handler)

        # Test registering an error
