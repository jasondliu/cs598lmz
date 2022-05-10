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

class Test_unicode_internal(unittest.TestCase):

    def test_utf16_be_decode(self):
        self.assertEqual(
            '\ud800\udc00',
            '\x00\xd8\x00\xdc'.decode('utf-16-be', 'surrogatepass'))
        self.assertEqual(
            '\ud800\udc00',
            '\x00\xd8\x00\xdc'.decode('utf-16-be', 'replace'))
        self.assertEqual(
            '\ud800\udc00',
            '\x00\xd8\x00\xdc'.decode('utf-16-be', 'ignore'))
        self.assertEqual(
            '\ud800\udc00',
            '\x00\xd8\x00\xdc'.decode('utf-16-be', 'xmlcharrefreplace'))
        self.assertEqual(
            '\ud800\udc00',
            '\x00
