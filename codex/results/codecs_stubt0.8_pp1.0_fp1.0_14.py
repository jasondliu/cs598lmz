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

class CodecTest(object):
    def test_simple_encode(self):
        self.assertEqual(self.codec.encode('abcdef'), (b'abcdef', 6))
        self.assertEqual(self.codec.encode('abcdef', 'strict'), (b'abcdef', 6))
        self.assertRaises(UnicodeEncodeError, self.codec.encode,
                          "\ud800", "strict")
        self.assertEqual(self.codec.encode("\ud800", "ignore"), (b"", 0))
        self.assertEqual(self.codec.encode("\ud800", "replace"), (b"?", 1))
        self.assertEqual(self.codec.encode("\ud800", "add_one_codepoint"),
                         (b'a\ud800', 3))
        self.assertEqual(self.codec.encode("\ud800", "add_utf16_bytes"),
                         (b'ab\ud800', 4))
        self.
