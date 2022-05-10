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

class Test_codecs(unittest.TestCase):

    def test_register_error(self):
        # Test that the error handler is called, and that the
        # replacement is properly encoded.
        self.assertEqual(b"\xff\xff\xff\xff".decode("utf-32-be", "add_one_codepoint"), "\uffff")
        self.assertEqual(b"\xff\xff\xff\xff".decode("utf-32-be", "add_utf16_bytes"), "\uffff\uffff")
        self.assertEqual(b"\xff\xff\xff\xff".decode("utf-32-be", "add_utf32_bytes"), "\uffff\uffff\uffff\uffff")

    def test_charmap_decode(self):
        self.assertEqual(b'abc'.decode('charmap'), 'abc')
        self.assertEqual(b'\x00\x01\x02'.decode('charmap'), '\x00\x01\x02
