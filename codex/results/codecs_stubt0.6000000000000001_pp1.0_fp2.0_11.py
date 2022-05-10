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

class TestCPPExceptions(unittest.TestCase):
    def test_add_one_codepoint(self):
        self.assertEqual(b'\xe4\xb8\x80'.decode("utf-8", "add_one_codepoint"),
                         b'\xe4\xb8\x80a'.decode("utf-8"))

    def test_add_utf16_bytes(self):
        self.assertEqual(b'\xe4\xb8'.decode("utf-8", "add_utf16_bytes"),
                         b'\xe4\xb8ab'.decode("utf-8"))

    def test_add_utf32_bytes(self):
        self.assertEqual(b'\xe4\xb8'.decode("utf-8", "add_utf32_bytes"),
                         b'\xe4\xb8abcd'.decode("utf-8"))

    def test_utf8_decode(self):
        self.assertEqual(b'\xe4\xb8\x80'.decode
