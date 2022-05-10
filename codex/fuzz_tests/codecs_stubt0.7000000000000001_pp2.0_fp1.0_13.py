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

    def test_utf_16_be(self):
        codecs.utf_16_be_decode(b"\xff\xfe\x0a\x00")
        codecs.utf_16_be_decode(b"\xff\xfe\x0a\x00", final=True)
        codecs.utf_16_be_decode(b"\x0a\x00", final=True)
        codecs.utf_16_be_decode(b"\x0a\x00")
        codecs.utf_16_be_decode(b"\x0a\x00\xfe\xff", final=True)
        codecs.utf_16_be_decode(b"\x0a\x00\xfe\xff")
        codecs.utf_16_be_decode(b"\x0a")

        self.assertRaises(UnicodeDecodeError, codecs.utf_16_be_decode, b"\xff")
