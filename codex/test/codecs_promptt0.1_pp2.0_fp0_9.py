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
        def handler2(exception):
            return (u'', exception.end)
        codecs.register_error('test.myerrorhandler', handler2)
        self.assertEqual(codecs.lookup_error('test.myerrorhandler'), handler2)
        # Test registering an error handler with a name that already exists
        # but with a different error handler
        def handler3(exception):
            return (u'', exception.end)
