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

class ReplTest(unittest.TestCase):

    def test_codec_error_call(self):
        self.assertEqual(b'\xe6'.decode('ascii', 'add_one_codepoint'), '\xe6a')
        self.assertEqual(b'\xe6'.decode('utf-16', 'add_utf16_bytes'), 'a\xe6')
        self.assertEqual(b'\xe6'.decode('utf-32', 'add_utf32_bytes'), 'a\xe6')
        self.assertEqual(b'\xe6'.decode('utf-32-be', 'add_utf32_bytes'), 'a\xe6')

    def test_function_error_call(self):
        self.assertEqual(b'\xe6'.decode('ascii', add_one_codepoint), '\xe6a')
        self.assertEqual(b'\xe6'.decode('utf-16', add_utf16_bytes), 'a\xe6')
        self
