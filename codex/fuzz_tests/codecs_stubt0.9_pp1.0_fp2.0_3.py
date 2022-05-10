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

class IncrementalWriterTestCase(unittest.TestCase):

    def test_utf8_encode(self):
        codec = codecs.lookup('utf-8')
        errors = ['strict', 'ignore', 'replace', 'xmlcharrefreplace',
                  'backslashreplace', 'add_one_codepoint', 'add_utf16_bytes']
        for errors in errors:
            codec.incrementalencoder(errors).encode('abc')
        self.assertRaises(UnicodeEncodeError,
                          codec.incrementaldecoder(errors).decode,
                          'abc')

    def test_utf16_le_encode(self):
        codec = codecs.lookup('utf-16-le')
        errors = ['strict', 'ignore', 'replace', 'xmlcharrefreplace',
                  'backslashreplace', 'add_one_codepoint', 'add_utf16_bytes',
                  'add_utf32_bytes']
        for errors in errors:
            codec.incrementalencoder(errors).encode('
