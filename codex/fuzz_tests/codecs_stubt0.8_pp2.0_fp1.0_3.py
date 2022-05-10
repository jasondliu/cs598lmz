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

class UnicodeDecodeTest(unittest.TestCase):

    def test_utf16_decode(self):
        x = 'ab\udc00cd\u1234'.encode('utf-16')
        u = x.decode('utf-16', 'surrogatepass')
        self.assertEqual(u, 'ab\udc00cd\u1234')

    def test_utf32_decode(self):
        x = 'ab\udc00cd\u1234'.encode('utf-32')
        u = x.decode('utf-32', 'surrogatepass')
        self.assertEqual(u, 'ab\udc00cd\u1234')

    def test_utf16_decode_replace(self):
        x = 'ab\ud800cd\ud800'.encode('utf-16')
        u = x.decode('utf-16', 'replace')
        self.assertEqual(u, 'ab\ufffdd800cd\ufffdd800')
 
    def test_utf16_
