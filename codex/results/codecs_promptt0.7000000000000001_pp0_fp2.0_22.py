import codecs
# Test codecs.register_error ()
#

import codecs
import codecs_test_support
import string

class TestRegisterError:
    def test_noncallable(self):
        self.assertRaises(TypeError, codecs.register_error, "a")

    def test_errors(self):
        # Test errors
        self.assertRaises(TypeError, codecs.register_error, "test", 1)
        self.assertRaises(TypeError, codecs.register_error, "test", lambda x: x)
        self.assertRaises(TypeError, codecs.register_error, "test",
                          lambda x, y: x)
        self.assertRaises(TypeError, codecs.register_error, "test",
                          lambda x, y, z: x)

    def test_lookup_error(self):
        # Test that the registered error handler is returned
        f = lambda x, y: None
        codecs.register_error("test", f)
        self.assertEqual(codecs.lookup_error("test"), f)

    def
