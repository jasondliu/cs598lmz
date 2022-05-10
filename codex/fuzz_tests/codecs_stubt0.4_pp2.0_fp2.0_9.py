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

    def test_decode_error_attributes(self):
        ue = UnicodeDecodeError("utf-8", b"\xff", 0, 1, "ouch")
        self.assertEqual(ue.encoding, "utf-8")
        self.assertEqual(ue.object, b"\xff")
        self.assertEqual(ue.start, 0)
        self.assertEqual(ue.end, 1)
        self.assertEqual(ue.reason, "ouch")
        self.assertEqual(ue.args, ("utf-8", b"\xff", 0, 1, "ouch"))

    def test_decode_error_str(self):
        ue = UnicodeDecodeError("utf-8", b"\xff", 0, 1, "ouch")
        self.assertEqual(str(ue), "'utf-8' codec can't decode byte 0xff in position 0: ouch")

    def test_decode_error_unicode(self):
        u
