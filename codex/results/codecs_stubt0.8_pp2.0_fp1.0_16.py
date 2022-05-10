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

class TestLatin1(unittest.TestCase):
    def test_overlong(self):
        out = []
        inp = b'\xc0\x80'
        dec = codecs.getincrementaldecoder("latin1", "add_one_codepoint")()
        for c in inp:
            out.append(dec.decode(c))
        out.append(dec.decode(b'', True))
        self.assertEqual(out, ['a', '\x00\x00'])

    def test_utf8(self):
        out = []
        inp = b'abc'
        dec = codecs.getincrementaldecoder("latin1", "replace")()
        for c in inp:
            out.append(dec.decode(c))
        out.append(dec.decode(b'', True))
        self.assertEqual(out, ['a', 'b', 'c'])
        enc = codecs.getincrementalencoder("latin1")()
        self.
