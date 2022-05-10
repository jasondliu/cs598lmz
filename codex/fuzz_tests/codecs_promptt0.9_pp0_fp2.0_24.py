import codecs
# Test codecs.register_error() (test_codecs test_register_error)
from test import test_support
import unittest

class CodecRegistryTest(unittest.TestCase):

    def test_register_error(self):
        # Testing register_error
        import codecs
        class X:
            def __init__(self, name):
                self.name = 'x'
            def __call__(self, encoding_error):
                return (u'', encoding_error.end)
        codecs.register_error('test.x', X)
        x = codecs.lookup_error('test.x')
        self.assertEqual(x.__class__, X)
        self.assertEqual(x.name, 'x')
        # reregistering should be ok
        codecs.register_error('test.x', X)
        self.assertEqual(x.__class__, X)
        self.assertEqual(x.name, 'x')
        def test(encoding_errors):
            self.called = None
            codecs.register_
