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

class DecoderTest(unittest.TestCase):

    def test_gb18030(self):
        # encoding
        self.assertEqual(b'\x95\x33\x86\x42',
                         '\u9646\u6D66'.encode('gb18030'))
        self.assertEqual(b'\xD2\xBB\xB0\xAE',
                         '\u5317\u4EAC'.encode('gb18030'))
        self.assertEqual(b'\x8E\x4F\x8E\xE7',
                         '\u6D4B\u8BD5'.encode('gb18030'))

        # decoding
        self.assertEqual('\u9646\u6D66',
                         b'\x95\x33\x86\x42'.decode('gb18030'))
        self.assertEqual('\u5317\u4EAC',
                         b'\xD2\xBB\xB0\xAE'.decode('
