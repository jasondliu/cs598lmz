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

    def test_decode(self):
        self.assertEqual(codecs.decode(b'abc', 'utf-8'), 'abc')
        self.assertEqual(codecs.decode(b'abc', 'utf-8', 'strict'), 'abc')
        self.assertEqual(codecs.decode(b'abc', 'utf-8', 'replace'), 'abc')
        self.assertEqual(codecs.decode(b'abc', 'utf-8', 'ignore'), 'abc')
        self.assertEqual(codecs.decode(b'abc', 'utf-8', 'add_one_codepoint'), 'aabc')
        self.assertEqual(codecs.decode(b'abc', 'utf-8', 'add_utf16_bytes'), 'aabc')
        self.assertEqual(codecs.decode(b'abc', 'utf-8', 'add_utf32_bytes'), 'aabc')

    def
