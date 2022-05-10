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


class TestRegrLib(unittest.TestCase):
    def test_decoder_state_after_decode(self):
        dec = codecs.getincrementaldecoder("utf-16")()
        # empty input
        self.assertRaises(UnicodeDecodeError, dec.decode, "", True)
        # enough input
        self.assertEqual(dec.decode(b'\xff'), "\ufffd")
        # output capped
        self.assertEqual(dec.decode(b'\xfeba'), "\U000eba")
        self.assertEqual(dec.decode(b'c\xffr', True), "\U000ebac\ufffdr")
        # adjust error position by offset
        self.assertEqual(dec.decode(b'\xff', True, 2), "\u0002\ufffd")
        # always expecting input
        self.assertEqual(dec.decode(b'a'), "\U000ebac\ufffdr\u0002a\ufffd")
        self.assertEqual(
