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

class TestDecodingInput(unittest.TestCase):
    #
    # Test decoding from various non-string types
    #

    def test_decoding_from_bytes_to_bytes(self):
        # Test decoding from bytes to bytes
        for encoding in ["ascii", "latin-1", "utf-8"]:
            self.assertEqual(b"abc", codecs.decode(b"abc", encoding))
            self.assertEqual(b"abc", codecs.decode(memoryview(b"abc"), encoding))

    def test_decoding_from_bytes_to_str(self):
        # Test decoding from bytes to str
        for encoding in ["ascii", "latin-1", "utf-8"]:
            self.assertEqual("abc", codecs.decode(b"abc", encoding))
            self.assertEqual("abc", codecs.decode(memoryview(b"abc"), encoding))

    def test_decoding_from_bytearray_to_bytes(self):
        # Test decoding from
