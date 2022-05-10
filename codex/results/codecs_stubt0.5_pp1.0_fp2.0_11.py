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

class CodecTest(unittest.TestCase):
    def test_utf7(self):
        # UTF-7 codec
        encoder = codecs.getencoder("utf-7")
        self.assertEqual(encoder("abc"), ("abc", 3))
        self.assertEqual(encoder("abc\u20acdef"), ("abc+AOQ-def", 9))
        self.assertEqual(encoder("\u20acdef"), ("+AOQ-def", 7))
        self.assertEqual(encoder("\u20acdef", "replace"), ("+AOQ-def", 7))
        self.assertEqual(encoder("\u20acdef", "ignore"), ("def", 3))
        self.assertEqual(encoder("\u20acdef", "xmlcharrefreplace"),
                         ("&#8364;def", 11))
        self.assertEqual(encoder("\u20acdef", "add_one_codepoint"),
                         ("+AOQ-defa", 8))
        self.assertE
