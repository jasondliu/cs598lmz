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

    def test_decode_error_handling(self):
        # Issue #11649: test that the correct number of bytes are consumed
        # when an error handler is used.
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            for error_handler in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                                  'add_utf16_bytes', 'add_utf32_bytes'):
                for input, expected in (
                        (b'\x00\x00\x00\x00\x00\x00\x00\x00', '\U000f0000'),
                        (b'\x00\x00\x00\x00\x00\x00\x00', '\U000f0000'),
                        (b'\x00\x00\x00\x00\x00\x00', '\U000f0000'),
                        (b'\x00\x00\x00\x00\x00', '
