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

class TestUnicodeDecodeError(unittest.TestCase):

    def test_unicode_decode_error(self):
        # Issue #11162: UnicodeDecodeError should have a reason attribute
        ude = UnicodeDecodeError("ascii", b"\xff", 1, 2, "ouch")
        self.assertEqual(ude.reason, "ouch")
        self.assertEqual(str(ude), "'ascii' codec can't decode byte 0xff in position 1: ouch")
        self.assertEqual(repr(ude),
                         "UnicodeDecodeError('ascii', b'\\xff', 1, 2, 'ouch')")

    def test_unicode_decode_error_unicode_reason(self):
        # Issue #11162: UnicodeDecodeError should have a reason attribute
        ude = UnicodeDecodeError("ascii", b"\xff", 1, 2, "\N{GREEK CAPITAL LETTER DELTA}")
        self.assertEqual(ude.reason, "\N{GREEK CAP
