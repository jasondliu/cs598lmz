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
    # Tests for the UTF-16 and UTF-32 codecs

    # XXX: test the MBCS codecs as well!

    def test_utf16_basics(self):
        u = chr(0x10000) + chr(0x10001)
        self.assertEqual(u.encode("utf-16"), b"\xd8\x00\xdc\x01")
        self.assertEqual(u.encode("utf-16be"), b"\x00\xd8\x01\xdc")
        self.assertEqual(u.encode("utf-16le"), b"\xd8\x00\xdc\x01")
        self.assertEqual(b"\xd8\x00\xdc\x01".decode("utf-16"), u)
        self.assertEqual(b"\x00\xd8\x01\xdc".decode("utf-16be"), u)
        self.assertEqual(b"\xd8\x00
