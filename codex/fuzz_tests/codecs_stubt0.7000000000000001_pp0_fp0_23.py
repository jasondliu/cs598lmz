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

class TestUnicode(unittest.TestCase):

    def test_decode(self):
        self.decode_helper("utf-8", "a", "a")
        self.decode_helper("utf-8", "a\x80", "a\ufffd")
        self.decode_helper("utf-8", "\x80", "\ufffd")
        self.decode_helper("utf-8", "a\xc0", "a\ufffd")
        self.decode_helper("utf-8", "\xc0", "\ufffd")
        self.decode_helper("utf-8", "a\xc0\x80", "a\ufffd\ufffd")
        self.decode_helper("utf-8", "\xc0\x80", "\ufffd\ufffd")
        self.decode_helper("utf-8", "a\xc1", "a\ufffd")
        self.decode_helper("utf-8", "\xc1", "\ufffd")
        self.decode
