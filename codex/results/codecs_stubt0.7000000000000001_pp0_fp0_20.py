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

class TestUTF16(unittest.TestCase):
    def test_decode_utf16_error_handling(self):
        # Test that UTF-16 decode errors are reported correctly
        # Issue #1737: UTF-16-LE with no BOM
        self.assertEqual(codecs.utf_16_le_decode(b'\xff\x00', 'strict', True),
                         ('\ufffd', 2))
        self.assertEqual(codecs.utf_16_le_decode(b'\xff\x00\x00', 'strict', True),
                         ('\ufffd\x00', 2))
        self.assertEqual(codecs.utf_16_le_decode(b'\xff\x00\x00', 'replace', True),
                         ('\ufffd\ufffd', 2))
        self.assertEqual(codecs.utf_16_le_decode(b'\xff\x00\x00', 'ignore', True),
                         ('\x00', 2))
        self.
