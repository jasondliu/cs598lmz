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
    def test_decode_unicode_error(self):
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            for errorhandler in ('replace', 'ignore', 'backslashreplace',
                                 'xmlcharrefreplace', 'surrogateescape',
                                 'surrogatepass', 'strict', 'add_one_codepoint',
                                 'add_utf16_bytes', 'add_utf32_bytes'):
                codecs.decode(b'\xff', encoding, errorhandler)
                codecs.decode(b'\xff\xff', encoding, errorhandler)
                codecs.decode(b'\xff\xff\xff', encoding, errorhandler)
                codecs.decode(b'\xff\xff\xff\xff', encoding, errorhandler)
                codecs.decode(b'\xff\xff\xff\xff\xff', encoding, errorhandler)
                codecs.decode(b'\xff\xff\xff\xff\xff
