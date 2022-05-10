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

class CodecsModuleTest(unittest.TestCase):
    # Tests for the codecs module itself

    def test_aliases(self):
        # Test the codec aliases
        self.assertEqual(codecs.lookup('latin-1'),
                         codecs.lookup('iso-8859-1'))
        self.assertEqual(codecs.lookup('iso-latin-1'),
                         codecs.lookup('iso-8859-1'))
        self.assertEqual(codecs.lookup('latin_1'),
                         codecs.lookup('iso8859_1'))

        self.assertEqual(codecs.lookup('utf-8'),
                         codecs.lookup('utf8'))

        self.assertEqual(codecs.lookup('utf-16'),
                         codecs.lookup('utf16'))

        self.assertEqual(codecs.lookup('utf-16-le'),
                         codecs.lookup('utf-16le'))
        self.assertEqual
