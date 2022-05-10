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
    def test_decode(self):
        # Test UnicodeDecodeError handling
        # Test the following codecs:
        # - utf-7
        # - utf-8
        # - utf-16-le
        # - utf-16-be
        # - utf-32-le
        # - utf-32-be
        # - unicode-escape
        # - raw-unicode-escape
        # - latin-1
        # - mbcs
        # - ascii
        # - base64-codec
        # - quopri-codec
        # - uu-codec
        # - hex-codec
        # - string-escape

        # utf-7
        self.assertEqual("+-", "a+-b".decode("utf-7"))
        self.assertEqual("+-", "a+-b".decode("utf-7", "ignore"))
        self.assertEqual("+-", "a+-b
