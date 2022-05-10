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

class UTF8_ExceptionTests(unittest.TestCase):
    def test_add_one_codepoint(self):
        self.assertEqual(b'ab\xc3\xa4'.decode('utf-8', 'add_one_codepoint'),
                         'ab\N{LATIN SMALL LETTER A WITH DIAERESIS}')
    def test_add_utf16_bytes(self):
        self.assertEqual(b'ab\xc3\xa4'.decode('utf-8', 'add_utf16_bytes'),
                         'ab\N{LATIN SMALL LETTER A WITH DIAERESIS}')
    def test_add_utf32_bytes(self):
        self.assertEqual(b'ab\xc3\xa4'.decode('utf-8', 'add_utf32_bytes'),
                         'ab\N{LATIN SMALL LETTER A WITH DIAERESIS}')

class UTF8_EncodeTests(unittest.TestCase):
    def test_encode1
