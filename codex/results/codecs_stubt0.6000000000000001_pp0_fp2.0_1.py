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
    def test_bug_5845(self):
        # Test that codecs.open() doesn't raise a SystemError when
        # the file position is negative.
        with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-16-le') as f:
            f.write('p\x00y\x00t\x00h\x00o\x00n\x00\x00\x00')
            f.seek(-3, os.SEEK_CUR)
            f.read()

    def test_utf7(self):
        # Test UTF-7 codec
        self.assertEqual(
            'A\u2262\u0391.',
            'A+ImIDkQ.'.encode('utf-7').decode('utf-7'))
        # RFC2152 example
        self.assertEqual(
            'Hi Mom -\u263a-!',
            'Hi Mom -+Jjo--!'.encode('utf-7').decode
