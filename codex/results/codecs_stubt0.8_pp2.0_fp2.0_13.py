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

def codec_name(codec):
    return codec.name

def codec_transform_encode(codec):
    return codec.encode

def codec_transform_decode(codec):
    return codec.decode

class CodecTest(unittest.TestCase):
    def test_utf_16_exception(self):
        self.assertEqual(b"ab\xff\xfeA\x00".decode("utf_16", "add_utf16_bytes"), "abA")

    def test_utf_16_le_exception(self):
        self.assertEqual(b"ab\xfe\xff\x00A".decode("utf_16_le", "add_utf16_bytes"), "abA")

    def test_utf_16_be_exception(self):
        self.assertEqual(b"ab\xff\xfe\x00A".decode("utf_16_be", "add_utf16_bytes"), "abA")

    def test_utf_32_exception(self):
       
