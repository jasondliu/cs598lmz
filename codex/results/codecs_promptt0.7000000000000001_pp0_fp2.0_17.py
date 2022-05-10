import codecs
# Test codecs.register_error()


class CodecTest(unittest.TestCase):
    codec = 'testcodec'

    def test_register_error(self):
        # Issue #15685: registering multiple errors for the same codec should
        # work, even if the error callback is a string and not a callable.
        error_handler = 'xmlcharrefreplace'
        codecs.register_error(error_handler, codecs.xmlcharrefreplace_errors)
        codecs.register_error(error_handler, codecs.backslashreplace_errors)
        codecs.register_error(error_handler, codecs.strict_errors)
        codecs.register_error(error_handler, codecs.ignore_errors)
        codecs.register_error(error_handler, codecs.replace_errors)

    @unittest.skipUnless(sys.platform == "win32", "Windows specific tests")
    def test_register_error_on_windows(self):
        # Issue #24261: registering multiple errors for the same codec should
        # work on Windows, even if the error callback is
