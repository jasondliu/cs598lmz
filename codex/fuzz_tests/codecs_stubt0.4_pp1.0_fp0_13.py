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

class TestUTF8(unittest.TestCase):
    def test_utf8_decode(self):
        self.assertEqual(b'abc'.decode('utf-8'), 'abc')
        self.assertEqual(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8'), '你好')
        self.assertEqual(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8', 'strict'), '你好')
        self.assertEqual(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8', 'replace'), '你好')
        self.assertEqual(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8', 'ignore'), '你好')
        self.assertEqual(b'\xe4\xbd\xa0\xe5\xa5\xbd
