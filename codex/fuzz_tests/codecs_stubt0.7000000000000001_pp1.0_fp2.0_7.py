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

class CodecsBytesTest(unittest.TestCase):
    def test_decode_error_handling(self):
        tests = [
            ("\xff", "\uFFFD"),
            ("\x80\xff\x7f", "\uFFFD\uFFFD\uFFFD"),
            ("\xff\x80\xff\x7f", "\uFFFD\uFFFD\uFFFD\uFFFD"),
            ("\x80\xff\x7f\xff", "\uFFFD\uFFFD\uFFFD\uFFFD"),
            ("\xff\x7f\xff\x80", "\uFFFD\uFFFD\uFFFD\uFFFD"),
            ("\x80\xff\x7f\xff\x80", "\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD"),
            ("\x80\xff\x7f\xff\x80\xff", "\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD"),
            ("
