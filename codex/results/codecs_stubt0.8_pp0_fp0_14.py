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

class CodingMapTest(unittest.TestCase):

    def test_replace(self):
        # issue 7972
        for encoding in ('utf-16', 'utf-32'):
            u = '\ufeff\xe9\u20ac'
            s = u.encode(encoding, 'replace')
            self.assertEqual(s.decode(encoding, 'replace'), u)

    def test_add_utf_byte(self):
        # issue 10589
        for encoding in ('utf-16', 'utf-32'):
            u = '\ufeff\xe9\u20ac'
            s = u.encode(encoding, 'add_utf16_bytes')
            self.assertEqual(s.decode(encoding, 'add_utf16_bytes'), u)
        for encoding in ('utf-16-le', 'utf-16-be', 'utf-32-le', 'utf-32-be'):
            u = '\ufeff\xe9\u20ac'
            s = u.encode(enc
