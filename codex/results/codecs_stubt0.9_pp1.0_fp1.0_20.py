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

class TestDecode(unittest.TestCase):
    def test_gbk(self):
        self.assertEqual("a\u4e00".encode("gbk", 'ignore'), b'a\xba\xc5')
        self.assertEqual("a\u4e00".encode("gbk", 'replace'), b'a?')
        self.assertEqual("a\u4e00".encode("gbk", 'xmlcharrefreplace'), b'a&#19990;')
        self.assertEqual("a\u4e00".encode("gbk", 'add_one_codepoint'), b'a\x00\x4e\x00\x00')
        self.assertEqual("a\u4e00".encode("gbk", 'add_utf16_bytes'), b'a\x00\x4e\x00\x00\x00\x42\x00')
        self.assertEqual("a\u4e00".encode("gbk", 'add_utf32_bytes'), b
