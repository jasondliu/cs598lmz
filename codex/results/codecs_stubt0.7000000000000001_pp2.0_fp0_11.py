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

class CodecsModuleTest(unittest.TestCase):
    def test_encode_decode(self):
        # codecs.encode(u"mystring", "rot_13")
        self.assertEqual(codecs.encode('abc', 'rot13'), 'nop')
        self.assertEqual(codecs.encode('\xff', 'hex'), 'c3bf')
        self.assertEqual(codecs.encode('\xff\xfe\x00\x01\x02\x03', 'hex_codec'), 'fffe00010203')
        self.assertEqual(codecs.encode('\xc2\x81', 'raw_unicode_escape'), '\\u0081')
        self.assertEqual(codecs.encode('\xc2\x81', 'unicode_escape'), '\\u0081')
        self.assertEqual(codecs.encode('\xc2\x81', 'unicode_internal'), '\x81')
        self.assertEqual(
