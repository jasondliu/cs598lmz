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

    def test_utf8_decode(self):
        # Test decoding with utf-8
        self.assertEqual('\u3042', '\xe3\x81\x82'.decode('utf-8'))
        self.assertEqual('\u3042\u3044', '\xe3\x81\x82\xe3\x81\x84'.decode('utf-8'))
        self.assertEqual('\u3042\u3044', '\xe3\x81\x82\xe3\x81\x84'.decode('utf-8'))
        self.assertEqual('\u3042\u3044', '\xe3\x81\x82\xe3\x81\x84'.decode('utf-8'))
        self.assertEqual('\u3042\u3044', '\xe3\x81\x82\xe3\x81\x84'.decode('utf-8'))
        self.assert
