import codecs
# Test codecs.register_error to replace codecs.strict errors
# with codecs.replace errors.

import codecs
import encodings
import test.test_support

class TestBase:
    def test_register_error(self):
        # Test that the codecs.strict errors are replaced by
        # codecs.replace errors.
        codecs.register_error("strict", codecs.replace_errors)
        self.assertRaises(UnicodeDecodeError, self.codec.decode,
                          "\xff", "strict")
        self.assertRaises(UnicodeEncodeError, self.codec.encode,
                          unichr(0xffff), "strict")
        self.assertRaises(UnicodeTranslateError, self.codec.decode,
                          "\xff", "strict", "strict")
        self.assertRaises(UnicodeTranslateError, self.codec.encode,
                          unichr(0xffff), "strict", "strict")

class TestUTF8(TestBase, un
