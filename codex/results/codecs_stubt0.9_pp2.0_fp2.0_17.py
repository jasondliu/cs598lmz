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

class TestUTF7(unittest.TestCase):

    def test_encode(self):
        encode = codecs.getencoder('utf-7')
        self.assertTrue(encode(u'hello') == (b'hello', 5))
        self.assertTrue(encode(u'hello', 'strict') == (b'hello', 5))
        self.assertTrue(encode(u'hello', 'replace') == (b'hello', 5))
        self.assertTrue(encode(u'hello', 'ignore') == (b'hello', 5))
        self.assertTrue(encode(u'hello', 'add_one_codepoint') == (b'hello', 5))
        self.assertTrue(encode(u'hello', 'add_utf16_bytes') == (b'hello', 5))
        self.assertTrue(encode(u'hello', 'add_utf32_bytes') == (b'hello', 5))

        self.assertTrue(encode(u'\ue863', 'strict') == (b'+AP
