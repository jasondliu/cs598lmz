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
        # Test that the error handling works correctly
        #
        # The test data is a UTF-8 encoded string with one byte
        # missing at the end.
        data = b'\xc3\xa9\n'
        self.assertRaises(UnicodeDecodeError, data.decode, "utf-8")
        self.assertEqual(data.decode("utf-8", "strict"),
                         u'\xe9\n')
        self.assertEqual(data.decode("utf-8", "ignore"),
                         u'\xe9\n')
        self.assertEqual(data.decode("utf-8", "replace"),
                         u'\xe9\ufffd\n')
        self.assertEqual(data.decode("utf-8", "backslashreplace"),
                         u'\\xe9\\x0a')
        self.assertEqual(data.decode("utf-8", "xmlchar
