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

# this is a test for the UTF-16 decoder
class TestUTF16(unittest.TestCase):

    def test_partial(self):
        self.assertRaises(UnicodeDecodeError, 'abc'.encode, 'utf-16', 'strict',
                          'abc'.encode('utf-16')[:-1])

    def test_partial_with_surrogates(self):
        self.assertRaises(UnicodeDecodeError, '\U00012345'.encode, 'utf-16', 'strict',
                          '\U00012345'.encode('utf-16')[:-1])

    def test_partial_with_surrogates_2(self):
        self.assertRaises(UnicodeDecodeError, '\U00012345'.encode, 'utf-16', 'strict',
                          '\U00012345'.encode('utf-16')[:-2])

    def test_partial_with_surrogates_3(self):
        self.assertRaises(UnicodeDecode
