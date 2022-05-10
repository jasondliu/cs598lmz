import codecs
# Test codecs.register_error
import array

class CodecsTests(unittest.TestCase):

    # Simple tests to check that the default encoding and
    # error handler are set as expected.

    def setUp(self):
        self.errors = [None, 'strict', 'replace', 'ignore', 'xmlcharrefreplace']

    def test_default_encodings(self):
        self.assertEqual(sys.getdefaultencoding(), 'utf-8')
        self.assertEqual(sys.getfilesystemencoding(), 'utf-8')
        self.assertEqual(locale.getpreferredencoding(), 'ANSI_X3.4-1968')

    def test_register_error(self):
        # dumb insanity check
        bytes = []
        errors = []
        for error in self.errors:
            bytes.append(b'x'*10)
            errors.append(error)

        # unicode-escape and its aliases are stupid, but if you really
        # want to test them, this is how you can do it:
        for error in ['unicode-escape
