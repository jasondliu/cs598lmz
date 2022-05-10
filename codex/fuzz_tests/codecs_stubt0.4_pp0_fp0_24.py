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

class TestCodecs(unittest.TestCase):

    def test_utf16_be(self):
        self.assertEqual(codecs.utf_16_be_encode("abc"), (b'\x00a\x00b\x00c', 3))
        self.assertEqual(codecs.utf_16_be_encode("abc", "add_one_codepoint"), (b'\x00a\x00b\x00c\x00a', 4))
        self.assertEqual(codecs.utf_16_be_encode("abc", "add_utf16_bytes"), (b'\x00a\x00b\x00c\x00a\x00b', 5))
        self.assertEqual(codecs.utf_16_be_encode("abc", "add_utf32_bytes"), (b'\x00a\x00b\x00c\x00a\x00b\x00c\x00d', 7))

        self.assertEqual(codecs
