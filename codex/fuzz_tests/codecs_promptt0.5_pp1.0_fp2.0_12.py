import codecs
# Test codecs.register_error()
from test import test_support
import unittest

class CodecRegistryTest(unittest.TestCase):

    def setUp(self):
        self.old_error_registry = codecs.error_registry.copy()

    def tearDown(self):
        codecs.error_registry.clear()
        codecs.error_registry.update(self.old_error_registry)

    def test_register_error(self):
        def my_error_handler(exception):
            return (u'', exception.end)
        codecs.register_error('my_error', my_error_handler)
        self.assertEqual(codecs.lookup_error('my_error'), my_error_handler)
        self.assertRaises(TypeError, codecs.register_error, 'my_error', 'blah')

    def test_lookup_error(self):
        self.assertEqual(codecs.lookup_error('strict'), codecs.strict_errors)
        self.assertEqual(codec
