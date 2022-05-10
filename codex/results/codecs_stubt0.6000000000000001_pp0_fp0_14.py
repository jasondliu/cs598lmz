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
    def test_utf8_decode(self):
        s = b'\xc3\xb1'
        u = s.decode("utf8")
        self.assertEqual(u, '\xf1')

        s = b'\xc3\xb1\xc3\xb1'
        u = s.decode("utf8")
        self.assertEqual(u, '\xf1\xf1')

        s = b'\xc3\xb1\xc3\xb1\xc3\xb1'
        u = s.decode("utf8")
        self.assertEqual(u, '\xf1\xf1\xf1')

        s = b'\xc3\xb1\xc3\xb1\xc3\xb1\xc3\xb1'
        u = s.decode("utf8")
        self.assertEqual(u, '\xf1\xf1\xf1\xf1')

        s = b'\xc3\xb1\xc
