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

class TestBase64(unittest.TestCase):
    def test_base64_encode(self):
        bs = b'\xFF\xFF\xFF\xFF'

        for w in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            for b64 in ['', '\n', '\r\n']:
                s = codecs.encode(bs, 'base64', b64)
                self.assertEqual(s, b'////' + b64)
                self.assertEqual(type(s), str)

            s = codecs.encode(bs, 'base64')
            self.assertEqual(s, b'////')
            self.assertEqual(type(s), bytes)

    def test_base64_decode(self):
        s = b'////'
        s2 = b'////\n'
        bs = b'\xFF\xFF\xFF\xFF'

        for b64 in ['', '\n', '\n\n',
