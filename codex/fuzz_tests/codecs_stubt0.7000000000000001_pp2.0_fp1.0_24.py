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

def utf16_bytes_to_unicode(exc):
    return (chr(exc.object[3])*2, exc.start+2)

def utf32_bytes_to_unicode(exc):
    return (chr(exc.object[1])*2, exc.start+4)

codecs.register_error("utf16_bytes_to_unicode", utf16_bytes_to_unicode)
codecs.register_error("utf32_bytes_to_unicode", utf32_bytes_to_unicode)

class TestUTF8(unittest.TestCase):
    def test_utf8_error(self):
        for encoding in ['utf-8', 'UTF8', 'uTf-8']:
            self.assertRaises(UnicodeDecodeError, '\xff'.decode, encoding)
            self.assertRaises(UnicodeDecodeError, '\xff'.decode, encoding, 'replace')
            self.assertRaises(UnicodeDecodeError, '\xff'.
