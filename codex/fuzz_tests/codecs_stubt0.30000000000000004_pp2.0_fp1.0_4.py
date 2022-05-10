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

class TestCodecs(unittest.TestCase):

    def test_utf8_decode_error_handling(self):
        # test that utf-8 codec handles decoding errors correctly
        # when reporting the error position
        s = b'\x80abc\x80'
        self.assertEqual(s.decode("utf-8", "strict"),
                         "\ufffdabc\ufffd")
        self.assertEqual(s.decode("utf-8", "replace"),
                         "\ufffdabc\ufffd")
        self.assertEqual(s.decode("utf-8", "ignore"),
                         "abc")
        self.assertEqual(s.decode("utf-8", "add_one_codepoint"),
                         "\ufffdabc\ufffd")
        self.assertEqual(s.decode("utf-8", "add_utf16_bytes"),
                         "\ufffdabc\ufffd")
        self.assertEqual(s.decode("utf-8", "add_utf32_bytes"),
                         "\uff
