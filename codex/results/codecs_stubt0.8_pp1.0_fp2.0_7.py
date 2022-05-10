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

class Test_UTF16_LE_Surrogates(unittest.TestCase):
    errors = ("strict", "ignore", "replace", "add_one_codepoint",
              "add_utf16_bytes", "add_utf32_bytes")

    # we just test the first 256 codepoints here, since all codepoints
    # are valid in UTF-16, so all these tests are equivalent for all
    # codepoints > 0xFFFF
    u = b"".join(b"%c%c" % (i, 0) for i in range(0x100))
    u_length = len(u) // 2
    x = b"".join(b"%c%c" % (i, 0) for i in range(0x100))
    x += b"\xdc\xd8\x01\x00\xdc\xd8\xff\xff"

    def test_decode(self):
        # decoding
        for errors in self.errors:
            u = self.u.decode("utf-16-le",
