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
    def test_codecs(self):
        self.assertEqual(codecs.decode('abc', 'ascii'), b'abc')
        self.assertEqual(codecs.decode(b'abc', 'ascii'), b'abc')
        self.assertEqual(codecs.encode('abc', 'ascii'), b'abc')
        self.assertEqual(codecs.encode(b'abc', 'ascii'), b'abc')
        self.assertEqual(codecs.escape_decode(b'abc'), (b'abc', 3))
        self.assertEqual(codecs.escape_decode(b'abc', 'strict'), (b'abc', 3))
        self.assertEqual(codecs.escape_encode(b'abc'), (b'abc', 3))
        self.assertEqual(codecs.escape_encode(b'abc', 'strict'), (b'abc', 3))

