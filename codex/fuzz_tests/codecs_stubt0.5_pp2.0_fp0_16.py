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

class TestErrorHandling(unittest.TestCase):

    def test_add_one_codepoint(self):
        for enc in ('utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'utf-32',
                    'utf-32-le', 'utf-32-be'):
            self.assertEqual('a\uFFFD', 'abc'.decode(enc, 'add_one_codepoint'))
            self.assertEqual(b'a\x00\x00\x00',
                             b'abcd'.decode(enc, 'add_one_codepoint'))

    def test_add_utf16_bytes(self):
        for enc in ('utf-16', 'utf-16-le', 'utf-16-be', 'utf-32',
                    'utf-32-le', 'utf-32-be'):
            self.assertEqual('a\uFFFD\uFFFD',
                             'abc'.decode(enc, 'add_utf16_bytes'))
