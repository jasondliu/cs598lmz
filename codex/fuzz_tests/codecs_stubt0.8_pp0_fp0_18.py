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

class UTF8Test(unittest.TestCase):

    def test_utf8(self):
        s = '\u3042\u3044\u3046\u3048\u304a'
        self.assertEqual(s.encode('utf8'), b'\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a')
        for enc in 'utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be':
            self.assertEqual(s.encode(enc, 'surrogatepass'), s.encode(enc))

        # error callback
        self.assertEqual(b'\xff'.decode('utf8', 'add_one_codepoint'), '\uFFFD')
        self.assertEqual(b'\xc3\xff'.decode('utf8', 'add_one_codepoint
