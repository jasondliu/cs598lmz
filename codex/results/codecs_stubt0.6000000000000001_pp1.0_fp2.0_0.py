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

class CodecTest(unittest.TestCase):
    def test_main(self):
        # UTF-8
        self.assertRaises(UnicodeDecodeError, 'abc'.decode, 'utf8', 'strict')
        self.assertEqual('a'.decode('utf8', 'add_one_codepoint'), 'a')
        self.assertRaises(UnicodeDecodeError, 'ab'.decode, 'utf8', 'add_one_codepoint')
        self.assertRaises(UnicodeDecodeError, 'abc'.decode, 'utf8', 'add_one_codepoint')
        self.assertEqual('a'.decode('utf8', 'ignore'), '')
        self.assertEqual('a'.decode('utf8', 'replace'), '\ufffd')
        self.assertEqual('ab'.decode('utf8', 'replace'), '\ufffd\ufffd')
        self.assertEqual('abc'.decode('utf8', 'replace'), '\ufffd\ufffd\ufffd')
