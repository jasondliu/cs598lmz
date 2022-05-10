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

class TestUTF16(unittest.TestCase):

    def test_utf16_decode(self):
        u = '\ud800\udc00'
        x = u.encode('utf-16')
        self.assertEqual(x, b'\x00\xd8\x00\xdc')
        self.assertEqual(x.decode('utf-16'), u)
        self.assertEqual(x.decode('utf-16-be'), u)
        self.assertEqual(x.decode('utf-16-le'), u)
        self.assertEqual(x.decode('utf-16-exact'), u)
        self.assertEqual(x.decode('utf-16-be-exact'), u)
        self.assertEqual(x.decode('utf-16-le-exact'), u)
        self.assertEqual(x.decode('utf-16-errorstrict'), u)
        self.assertEqual(x.decode('utf-16-be-errorstrict'),
