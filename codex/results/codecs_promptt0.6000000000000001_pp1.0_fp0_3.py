import codecs
# Test codecs.register_error()

import test_support, unittest, codecs

class TestRegistry(unittest.TestCase):

    def test_register(self):
        # Test registering an encoding error handler
        # This test is not exhaustive; the Codec base class
        # has additional tests.
        errors = 'test'
        handler = lambda exc: (u'', exc.end)
        oldhandler = codecs.lookup_error(errors)
        codecs.register_error(errors, handler)
        try:
            self.assertEqual(codecs.lookup_error(errors), handler)
            self.assertRaises(TypeError, codecs.register_error, 0, handler)
            self.assertRaises(TypeError, codecs.register_error, errors, 0)
            self.assertRaises(TypeError, codecs.register_error, errors, handler, 0)
            self.assertRaises(LookupError, codecs.lookup_error, 'xxx')
            self.assertRaises(TypeError, codecs.lookup_error, errors, 0)
