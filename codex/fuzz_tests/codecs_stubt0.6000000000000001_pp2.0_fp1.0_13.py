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

class ErrorHandlingTest(unittest.TestCase):

    def setUp(self):
        self.errors = []
        self.callbacks = []
        self.encoding = "ascii"
        self.test_string = "abc\xFF"
        self.test_unicode = "abc\u1234"

    def check_encode(self, input, errors, expected, callback=None):
        self.errors = []
        self.callbacks = []
        result = codecs.encode(input, self.encoding, errors)
        self.assertEqual(result, expected)
        self.assertEqual(self.errors, errors)
        self.assertEqual(self.callbacks, [callback])

    def check_decode(self, input, errors, expected, callback=None):
        self.errors = []
        self.callbacks = []
        result = codecs.decode(input, self.encoding, errors)
        self.assertEqual(result, expected)
        self.assertEqual(self.errors, errors
