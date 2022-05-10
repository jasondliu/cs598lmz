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
    def test_utf8(self):
        self.check_error_handle(
            codecs.getreader('utf-8'),
            codecs.getwriter('utf-8'),
            b"\xff",
            "\ufffd",
            "\uc0\u80ff",
            "\ufffd\x80\x80\x80",
            "\xed\xb2\x80\xed\xb0\x80",
            "\xed\xb2\x80\ufffd\x80\x80",
            "\ufce0\u8080",
            "\ufce0\ufffd\x80\x80",
            "\ufce0\u8080\ufffd",
            "\xed\xb2\x80\xed\xb0\x80\xed\xb2\x80",
            "\xed\xb2\x80\xed\xb0\x80\ufffd\x80\x80",
            "\xed\xb2\x80\ufffd\x80
