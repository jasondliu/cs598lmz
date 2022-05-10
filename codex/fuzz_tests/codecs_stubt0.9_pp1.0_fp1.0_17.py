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

class CJKCodecTest(unittest.TestCase):

    def test_replace(self):
        for encoding in 'euc-jp', 'euc-kr', 'hz', 'iso2022-jp', 'shift-jis':
            self.assertEqual("\ufffd", codecs.getdecoder(encoding)("a", "replace")[0])
            self.assertEqual("\ufffd\ufffd", codecs.getdecoder(encoding)("aa", "replace")[0])
            self.assertEqual("a\ufffd", codecs.getdecoder(encoding)("ab", "replace")[0])
            self.assertEqual("a\ufffd", codecs.getdecoder(encoding)("aba", "replace")[0])
            self.assertEqual("ab\ufffd", codecs.getdecoder(encoding)("abaa", "replace")[0])

        for encoding in 'big5', 'gb2312':
            self.assertEqual("\ufffd\ufffd", codecs.getdecoder
