import codecs
# Test codecs.register_error("test", codecs.replace_errors)
# Test codecs.register_error("test", codecs.xmlcharrefreplace_errors)
# Test codecs.register_error("test", codecs.namereplace_errors)
# Test codecs.register_error("test", codecs.strict_errors)
# Test codecs.register_error("test", codecs.ignore_errors)
# Test codecs.register_error("test", codecs.backslashreplace_errors)

class CodecsModuleTest(unittest.TestCase):
    # We're testing an external module, so we can't use self.assertRaises
    # instead, we'll use a global variable to store the exception info
    # and test that it is not None in each test.
    exception = None

    def setUp(self):
        # Clear the exception state
        self.exception = None

    def tearDown(self):
        # Make sure the exception state has been cleared by the test
        self.assertIsNone(self.exception)

    def _test_encode(self, input, errors
