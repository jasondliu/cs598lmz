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

class TestCodecs(unittest.TestCase):
    def setUp(self):
        if sys.byteorder != 'little':
            self.skipTest("not little endian")

    def check_codec(self, encoding):
        # try encoding
        u = "\udcba" # unpaired surrogates
        x = u.encode(encoding, errors='replace')
        self.assertEqual(x, b'?') # result is always 1 byte
        x = u.encode(encoding, errors='xmlcharrefreplace')
        self.assertEqual(x, b'&#56318;')
        x = u.encode(encoding, errors='ignore')
        self.assertEqual(x, b'')
        x = u.encode(encoding, errors='backslashreplace')
        self.assertEqual(x, b'\\udcba')
        x = u.encode(encoding, errors='surrogatepass')
        self.assertEqual(x, b'ab')
        x = u.en
