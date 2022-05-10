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


class UnicodeTranslateTests(unittest.TestCase):
    def test_decode_ascii(self):
        for input in (b"abc", "abc"):
            for errors in (None, "strict"):
                for output in (bytes, bytearray, memoryview):
                    with self.subTest(input=input, errors=errors, output=output):
                        self.assertEqual(input.decode("ascii", errors),
                                         output(input).decode("ascii", errors))
                        self.assertEqual(input.decode("ascii", errors),
                                         output(input, "ascii", errors))
                        self.assertEqual(input.decode("ascii", errors),
                                         output(input, "ascii").decode(errors))

    def test_encode_ascii(self):
        for input in ("abc", "abc\N{LATIN SMALL LETTER A WITH ACUTE}"):
            for errors in (None, "strict", "ignore", "replace",
