import codecs
# Test codecs.register_error by passing in a funny UnicodeError subclass and
# providing an error handler.
class FunnyUnicodeError(UnicodeError):
    """subclass of UnicodeError for testing purposes"""
    pass
class FunnyUnicodeDecodeError(UnicodeDecodeError):
    """subclass of UnicodeDecodeError for testing purposes"""
    pass


def handler(e):
    return ('spam', e.end)
FUNNY_ERROR = FunnyUnicodeError('spam', 'eggs', 42, 1337.0)
FUNNY_DECODE_ERROR = UnicodeDecodeError('ascii', b'spameggs', 42, 43, FUNNY_ERROR
    )


class ErrorRegisteringTestCase(unittest.TestCase):

    def setUp(self):
        self.saved_encodings = sys.getfilesystemencoding, sys.getdefaultencoding(
            )

    def tearDown(self):
        sys.getfilesystemencoding, sys.getdefaultencoding = self.saved_encodings

    def test_register_my_error(
