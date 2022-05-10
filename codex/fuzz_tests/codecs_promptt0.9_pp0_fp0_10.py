import codecs
# Test codecs.register_error("foo", )


class EncoderTest(unittest.TestCase):
    def check_class(self, test_class, input, errmsg='xxx'):
        """Encode string using given error handling class.

        Handles 8-bit strings only.
        """
        # Error handling
        result = test_class().encode(input)
        self.assertNotEqual(input, result)
        self.assertEqual(input.encode(encoding, test_class), result)
        self.assertEqual(input.encode(encoding, test_class.__name__), result)

    def test_identity(self):
        # No errors
        test_strings = [
            # Test BMP character
            b'abc\xe4\xf6\xfcdef',
            # Test lone surrogates
            b'abc\xed\xa0\x80def\xed\xb0\x80ghi',
        ]
        for string in test_strings:
            self.assertEqual(string.decode(encoding, 'identity'), string
