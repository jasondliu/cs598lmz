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

    def test_decode_add_one_codepoint(self):
        # Test the 'add_one_codepoint' error handler
        self.assertEqual(b"\x80".decode("ascii", "add_one_codepoint"), "a\x80")
        self.assertEqual(b"\xff".decode("ascii", "add_one_codepoint"), "a\xff")
        self.assertEqual(b"\x80\xff".decode("ascii", "add_one_codepoint"),
                         "a\x80a\xff")
        self.assertEqual(b"\x80\xff\x80\xff".decode("ascii", "add_one_codepoint"),
                         "a\x80a\xffa\x80a\xff")
        self.assertEqual(b"\x80\xff\x80\xff".decode("ascii", "add_one_codepoint"),
                        
