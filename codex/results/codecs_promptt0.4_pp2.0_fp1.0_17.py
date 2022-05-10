import codecs
# Test codecs.register_error
# http://bugs.python.org/issue1700

import codecs
import unittest

class TestRegisterError(unittest.TestCase):
    def test_register_error(self):
        # Example from the documentation
        def handler(exception):
            return (u'', exception.end)
        codecs.register_error('test.ignore', handler)
        self.assertEqual(codecs.lookup_error('test.ignore'), handler)
        self.assertEqual(codecs.lookup_error('test.ignore')(Exception(42)), ('', 42))

        # Test that the handler gets called
        def handler(exception):
            raise TypeError
        codecs.register_error('test.strict', handler)
        self.assertEqual(codecs.lookup_error('test.strict'), handler)
        self.assertRaises(TypeError,
                          codecs.lookup_error('test.strict'),
                          Exception(42))

        # Test that the handler gets called with the correct arguments
        def handler
