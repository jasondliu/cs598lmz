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

class TestDecode(unittest.TestCase):
    def test_decode_add_one_codepoint_utf8(self):
        # utf-8
        data = b'\xed\xb3\x9d\xed\xb3\x9d' # U+D55D U+D55D
        self.assertRaises(UnicodeDecodeError, data.decode, "utf-8", "add_one_codepoint")
        self.assertEqual('\U000d55da', data.decode("utf-8", "add_one_codepoint"))
        self.assertEqual('\U000d55da\U000d55d', data.decode("utf-8", "replace"))
        self.assertEqual('\U000d55da\U000d55d', data.decode("utf-8", "ignore"))
        self.assertEqual('\U000d55da\U000d55d', data.decode("utf-8", "backslashreplace"))
        self.assertE
