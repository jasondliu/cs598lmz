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

    def test_utf_8(self):
        self.assertEqual(codecs.decode(b'\x00\x00\x00a', 'utf_8'), '\x00\x00\x00a')
        self.assertEqual(codecs.decode(b'\x00\x00\x00', 'utf_8'), '\x00\x00\x00')
        self.assertEqual(codecs.decode(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 'utf_8'), '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(codecs.decode(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
