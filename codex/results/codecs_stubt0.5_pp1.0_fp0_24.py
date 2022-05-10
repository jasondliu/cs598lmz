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
    def test_utf8_errors(self):
        # Test utf8 codec
        self.assertEqual(codecs.getencoder("utf-8")("\ud800"), (b"\xed\xa0\x80", 1))
        self.assertEqual(codecs.getencoder("utf-8")("\udc00"), (b"\xed\xb0\x80", 1))
        self.assertEqual(codecs.getencoder("utf-8")("\ud800\udc00"), (b"\xf0\x90\x80\x80", 2))
        self.assertEqual(codecs.getencoder("utf-8")("\udbff\udfff"), (b"\xf4\x8f\xbf\xbf", 2))
        self.assertEqual(codecs.getencoder("utf-8")("\ud800\udc00", "replace"), (b"\xef\xbf\xbd\x
