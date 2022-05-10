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

class TestCodecs(unittest.TestCase):
    def test_decode_error_handling(self):
        # Test that the error handling callback is called with the correct
        # arguments
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            for error_handler in ('strict', 'replace', 'ignore'):
                for byte_string in (b'\xff', b'\xff\xff', b'\xff\xff\xff\xff'):
                    # The error handling callback should be called with the
                    # correct number of bytes
                    with self.subTest(encoding=encoding,
                                      error_handler=error_handler,
                                      byte_string=byte_string):
                        self.assertEqual(
                            byte_string.decode(encoding, error_handler),
                            byte_string.decode(encoding, 'add_one_codepoint'),
                        )

    def test_encode_error_handling(self):
        # Test that the error handling callback is called with the correct
       
