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

    def test_utf16_decode(self):
        # check that utf-16-le, utf-16-be, and utf-16-expat all decode
        # the same (and correctly)
        self.assertEqual(b"abc".decode("utf-16-le"), "abc")
        self.assertEqual(b"abc".decode("utf-16-be"), "abc")
        self.assertEqual(b"abc".decode("utf-16-expat"), "abc")

    def test_utf16_decode_error(self):
        # check that utf-16-le, utf-16-be, and utf-16-expat all decode
        # the same (and correctly)
        self.assertEqual(b"abc\xff".decode("utf-16-le", "strict"),
                         "\udcffabc")
        self.assertEqual(b"abc\xff".decode("utf-16-be", "strict"),
                        
