import codecs
# Test codecs.register_error

# This test is not exhaustive, but it should catch most of the
# problems.

import codecs
import sys
import unittest

class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        # Test registering an error handler
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.myerrorhandler', handler)
        self.assertEqual(codecs.lookup_error('test.myerrorhandler'), handler)
        self.assertRaises(LookupError, codecs.lookup_error, 'test.nosuchhandler')
        # Test registering an error handler with a wrong signature
        def handler(exception):
            return (u'', exception.end)
        self.assertRaises(TypeError, codecs.register_error, 'test.myerrorhandler', handler, True)
        # Test registering an error handler with a wrong signature
        def handler(exception):
            return (u'', exception.end)
        self.assertRaises(TypeError
