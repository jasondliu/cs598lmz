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
    encoding = "utf-32"

    def test_streamreader(self):
        r = codecs.getreader(self.encoding)(BytesIO(b''))
        self.assertEqual(r.read(), '')
        r = codecs.getreader(self.encoding)(BytesIO(b'ab'))
        self.assertRaises(UnicodeDecodeError, r.read)
        r = codecs.getreader(self.encoding)(BytesIO(b'ab'))
        self.assertEqual(r.read(), '\ufffd\ufffd\ufffd')
        r = codecs.getreader(self.encoding)(BytesIO(b'ab'))
        self.assertEqual(r.read(5), '\ufffd\ufffd\ufffd')
        r = codecs.getreader(self.encoding)(BytesIO(b'abc'))
        self.assertEqual(r.read(2), '\ufffd\ufffd')
        r = codecs
