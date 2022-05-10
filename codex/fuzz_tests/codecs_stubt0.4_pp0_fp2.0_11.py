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

class TestUnicodeDecode(unittest.TestCase):
    def test_decode_error_handling(self):
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            for error_handler in ('strict', 'ignore', 'replace', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
                for text in ('\xff', '\xff\xff', '\xff\xff\xff\xff'):
                    try:
                        codecs.decode(text, encoding, error_handler)
                    except UnicodeDecodeError:
                        self.fail("UnicodeDecodeError raised for encoding=%r, error_handler=%r" % (encoding, error_handler))

    def test_decode_error_handling_surrogatepass(self):
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            for error_handler in ('strict', 'ignore', 'replace'):
                for text in ('\xff', '\
