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

class CodecsModuleTest(unittest.TestCase):

    def test_bug_2636(self):

        # This should not cause the "RuntimeError: maximum recursion depth
        # exceeded" exception

        self.assertEqual('\r'.encode('ascii', 'add_one_codepoint'), b'\r')
        self.assertEqual('\r'.encode('ascii', 'add_utf16_bytes'), b'\r')
        self.assertEqual('\r'.encode('ascii', 'add_utf32_bytes'), b'\r')
        self.assertEqual('\r'.encode('utf-8', 'add_one_codepoint'), b'\r')
        self.assertEqual('\r'.encode('utf-8', 'add_utf16_bytes'), b'\r')
        self.assertEqual('\r'.encode('utf-8', 'add_utf32_bytes'), b'\r')
        self.assertEqual('\r'.encode('utf-16',
