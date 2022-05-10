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

class Test_Decoding(unittest.TestCase):

    def test_utf8_decode(self):
        # Test UTF-8 decoding

        # Trivial cases
        self.assertEqual("".encode("utf-8").decode("utf-8"), "")
        self.assertEqual("abc".encode("utf-8").decode("utf-8"), "abc")

        # Boundaries of 1-4 byte sequences
        for n in range(0x00, 0x80):
            self.assertEqual(chr(n).encode("utf-8").decode("utf-8"), chr(n))
        for n in range(0x00, 0x800, 0x77):
            self.assertEqual(chr(n).encode("utf-8").decode("utf-8"), chr(n))
        for n in range(0x0000, 0x10000, 0x7777):
            self.assertEqual(chr(n).encode("utf-8").decode("utf-8"), chr(n
