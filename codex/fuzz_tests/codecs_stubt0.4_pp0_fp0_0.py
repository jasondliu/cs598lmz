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

    def test_utf_16_exception(self):
        self.assertEqual(codecs.decode(b'\xff', 'utf-16', 'add_one_codepoint'),
                         'a')
        self.assertEqual(codecs.decode(b'\xff\xff', 'utf-16', 'add_one_codepoint'),
                         'a')
        self.assertEqual(codecs.decode(b'\xff', 'utf-16le', 'add_one_codepoint'),
                         'a')
        self.assertEqual(codecs.decode(b'\xff\xff', 'utf-16le', 'add_one_codepoint'),
                         'a')
        self.assertEqual(codecs.decode(b'\xff', 'utf-16be', 'add_one_codepoint'),
                         'a')
        self.assertEqual(codecs.decode(b'\xff\xff', 'utf
