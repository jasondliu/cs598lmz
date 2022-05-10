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

class TestUTF32(unittest.TestCase):
    def test_utf32(self):
        for encoding in ('utf-32-be', 'utf-32-le'):
            self.assertEqual(
                'abcd'.encode(encoding, 'add_utf32_bytes'),
                b'abcdabcd'
            )
            self.assertEqual(
                'abcd'.encode(encoding, 'add_utf32_bytes'),
                b'abcdabcd'
            )
            self.assertEqual(
                'abcd'.encode(encoding, 'add_one_codepoint'),
                b'abcdabcd'
            )
            self.assertEqual(
                'abcd'.encode(encoding, 'add_one_codepoint'),
                b'abcdabcd'
            )
            self.assertEqual(
                'abcd'.encode(encoding, 'replace'),
                b'abcdabcd'
            )
            self.assertEqual(
                'abcd'.
