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
    def test_utf_16_be_decode(self):
        self.assertEqual(
            '\u3042\u3044\u3046',
            codecs.utf_16_be_decode(b'\x30\x42\x30\x44\x30\x46', 'strict')[0]
        )
        self.assertEqual(
            '\u3042\u3044\u3046',
            codecs.utf_16_be_decode(b'\x30\x42\x30\x44\x30', 'strict')[0]
        )
        self.assertEqual(
            '\u3042\u3044\u3046',
            codecs.utf_16_be_decode(b'\x30\x42\x30\x44', 'strict')[0]
        )
        self.assertEqual(
            '\u3042\u3044\u3046',
            codecs
