import codecs
# Test codecs.register_error() and .lookup_error().
test_support.import_module('codecs')

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        # Test with a bogus error handler name.
        self.assertRaises(LookupError,
                          codecs.register_error, "xyzzy")
        # Test with an error handler that doesn't have the required signature
        # (takes too few arguments).
        self.assertRaises(TypeError,
                          codecs.register_error, "strict", lambda: True)
        # Test with an error handler that doesn't have the required signature
        # (takes too many arguments).
        self.assertRaises(TypeError,
                          codecs.register_error, "strict", lambda x, y, z: True)
        # Test with an error handler that doesn't have the required signature
        # (takes an argument with an inappropriate default value).
        self.assertRaises(TypeError,
                          codecs.register_error, "strict", lambda x, y
