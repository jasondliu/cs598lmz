import codecs
# Test codecs.register_error


def err(codec_name):
    """Make a one-off error handler that raises a UnicodeError."""
    def handler(exception):
        return ('', exception.start + 1)
    return handler


class TestRegisterError(unittest.TestCase):

    def test_register_error(self):
        codecs.register_error('test', err)
        self.assertEqual(codecs.lookup_error('test'), err)

    def test_unregister_error(self):
        codecs.register_error('test', err)
        self.assertEqual(codecs.lookup_error('test'), err)
        codecs.register_error('test', None)
        self.assertEqual(codecs.lookup_error('test'), codecs.strict_errors)

    def test_register_error_after_lookup(self):
        # Issue #3017
        codecs.register_error('test', err)
        self.assertEqual(codecs.lookup_error('test'), err)
        self
