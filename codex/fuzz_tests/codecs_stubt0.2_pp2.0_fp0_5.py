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

class TestUnicodeDecode(unittest.TestCase):

    def test_decode_error_handling(self):
        # Test various error handling schemes
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                           'add_utf16_bytes', 'add_utf32_bytes'):
                for input in (b'\xff', b'\xff\xff', b'\xff\xff\xff',
                              b'\xff\xff\xff\xff', b'\xff\xff\xff\xff\xff'):
                    if errors == 'add_one_codepoint':
                        expected = 'a'
                    elif errors == 'add_utf16_bytes':
                        expected = 'ab'
                    elif errors == 'add_utf32_bytes':
                        expected = 'abcd'
                    else:
                        expected = ''
                    self.assertEqual(input.decode(encoding, errors), expected)
                   
