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

class CodecTest(unittest.TestCase):

    def test_read_partial_utf8(self):
        """Test reading partial UTF-8 sequences"""
        reader = codecs.getreader("utf-8")
        text = reader(BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd'))
        self.assertEqual(text.read(1), '\u4f60')
        self.assertEqual(text.read(1), '\u597d')
        self.assertEqual(text.read(1), '')

    def test_read_partial_utf16(self):
        """Test reading partial UTF-16 sequences"""
        reader = codecs.getreader("utf-16-le")
        text = reader(BytesIO(b'\x60\x4f\x59\x7d'))
        self.assertEqual(text.read(1), '\u4f60')
        self.assertEqual(text.read(1), '\u597d')
        self.assertE
