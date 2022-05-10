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

class TestReplacementChars(unittest.TestCase):
    """
    https://github.com/python/cpython/pull/18339/
    """
    def setUp(self):
        self.TEST_STRING = "this is a test, 1234"

    def test_replacement_add_code_point(self):
        self.do_test(self.TEST_STRING, "add_one_codepoint", "this is a test, 1234\ufffd")

    def test_replacement_add_bytes_utf16(self):
        self.do_test(self.TEST_STRING, "add_utf16_bytes", "this is a test, 1234\ufffd\ufffd")

    def test_replacement_add_bytes_utf32(self):
        self.do_test(self.TEST_STRING, "add_utf32_bytes", "this is a test, 1234\ufffd\ufffd\ufffd\ufffd")

    def do_test(self, test_string, encoding, expected_
