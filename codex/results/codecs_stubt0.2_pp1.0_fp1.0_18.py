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

class TestDecode(unittest.TestCase):

    def test_decode_error_handling(self):
        # Test various error handling schemes
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            for errors in (None, 'strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
                # Encode a string with a lone surrogate
                x = '\ud800'
                y = x.encode(encoding, 'surrogatepass')
                self.assertEqual(x.encode(encoding, 'surrogatepass'), y)
                # Decode it with various error handling schemes
                if errors is None:
                    errors = 'strict'
                self.assertRaises(UnicodeDecodeError, y.decode, encoding)
                self.assertEqual(y.decode(encoding, errors),
                                 x.encode(encoding, errors).decode(encoding, errors))

    def test
