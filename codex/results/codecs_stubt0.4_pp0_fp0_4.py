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

class Test_utf_16_be_decoder(unittest.TestCase):
    def test_errors(self):
        self.assertEqual(
            codecs.utf_16_be_decode(b'\x00\x00', 'replace')[0],
            '\ufffd'
        )
        self.assertEqual(
            codecs.utf_16_be_decode(b'\x00\x00', 'ignore')[0],
            ''
        )
        self.assertEqual(
            codecs.utf_16_be_decode(b'\x00\x00', 'add_one_codepoint')[0],
            'a'
        )
        self.assertEqual(
            codecs.utf_16_be_decode(b'\x00\x00', 'add_utf16_bytes')[0],
            'ab'
        )
        self.assertEqual(
            codecs.utf_16_be_decode(b'\x00\x00', 'add_
