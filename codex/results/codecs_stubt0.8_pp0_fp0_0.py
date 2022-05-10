import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)


class Test_unicode_internal(unittest.TestCase):

    def test_utf8(self):
        """
        Issue #19688: decoding from utf-8 to unicode failed if the last character
        was a surrogate pair.
        """
        for char in range(0xD800, 0xE000):
            self.assertEqual(str(bytes([char]), 'utf-8', 'surrogatepass'),
                             chr(char))

    def test_bug_19668(self):
        """
        Issue #19668: decoding from utf-8 to unicode failed if the last character
        was a surrogate pair.
        """
        for char in range(0xD800, 0xE000):
            self.assertEqual(str(bytes([char]), 'utf-8', 'surrogatepass'),
                             chr(char))

    def test_bug_19835(self):
        """
        Issue #19835: decoding from utf-8 to unicode failed if the last character
        was a surrogate pair.
        """
       
