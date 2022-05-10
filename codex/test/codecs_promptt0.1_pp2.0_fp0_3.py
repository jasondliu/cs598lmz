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
        # Test registering an error handler with a name that already exists
        self.assertRaises(ValueError, codecs.register_error,
                          'test.myerrorhandler', handler)
        # Test registering an error handler with a name that already exists
        # but with force=True
        codecs.register_error('test.myerrorhandler', handler, True)
        self.assertEqual(codecs.lookup_error('test.myerrorhandler'), handler)
        # Test registering an error handler with a name that already exists
        # but with force=False
