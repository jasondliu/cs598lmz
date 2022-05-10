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

class TestErrorHandler(unittest.TestCase):

    def test_basics(self):
        s = "background text &#123;&ghk;&#123;\u0FF0\u0F2c&#123;{{% include page-test-start.html %}}"

        utf8_encoded = s.encode("utf-8")
        b = BitReader(utf8_encoded)
        br2 = b.clone_with_bytes(utf8_encoded)
        self.assertEqual(utf8_encoded,br2.bytes)
        self.assertEqual(0,br2.bitpos)
        self.assertEqual(0,br2.byteoffset)

        # make sure the two BitReader instances above return the same bytes for the same ranges
        for pos in range(len(utf8_encoded)):
            self.assertEqual(b.bytes[pos], br2.bytes[pos])
            for length in range(1, len(utf8_encoded)-pos):
                self.assertEqual(
