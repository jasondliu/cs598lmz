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
    def test_basics(self):
        self.assertRaises(LookupError, codecs.decode, "00112233", "ascii")

        self.assertEqual(codecs.decode(b"00112233", "hex"), b"\x00\x11\x22\x33")

        self.assertEqual(codecs.decode(b"00112233", "hex_codec"), b"\x00\x11\x22\x33")

        self.assertEqual(codecs.decode(b"00112233", "hex_codec2"), b"\x00\x11\x22\x33")

        self.assertEqual(codecs.decode(b"00112233", "hex_codec3"), b"\x00\x11\x22\x33")

        self.assertEqual(codecs.decode(b"00112233", "hex_codec4"), b"\x00\x
