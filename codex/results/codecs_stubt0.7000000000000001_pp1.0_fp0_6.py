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

class TestDecode_ErrorHandlers(unittest.TestCase):
    def test_decode_errors(self):
        # test decode error handling
        for encoding in ['ascii', 'utf-8', 'latin-1', 'utf-16', 'utf-32', 'utf-32-le', 'utf-16-le', 'utf-16-be', 'utf-32-be']:
            if encoding not in codecs.__all__:
                continue
            for errors in ['strict', 'ignore', 'replace', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes']:
                decoder = codecs.getincrementaldecoder(encoding)(errors=errors)
                if errors == 'strict':
                    self.assertRaises(UnicodeDecodeError, decoder.decode, b'\xff', True)
                    continue
                if errors == 'ignore':
                    self.assertEqual(decoder.decode(b'\xff', True), '')
                if errors == 'replace':
