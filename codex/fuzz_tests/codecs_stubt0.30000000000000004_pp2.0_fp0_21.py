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

    def test_ascii_decode(self):
        self.assertEqual(codecs.ascii_decode(b'abc'), ('abc', 3))
        self.assertEqual(codecs.ascii_decode(b'abc\0'), ('abc\x00', 4))
        self.assertEqual(codecs.ascii_decode(b'\xe4\xf6\xfc'), ('\xe4\xf6\xfc', 3))
        self.assertEqual(codecs.ascii_decode(b'\xe4\xf6\xfc', 'ignore'), ('', 3))
        self.assertEqual(codecs.ascii_decode(b'\xe4\xf6\xfc', 'replace'), ('?\ufffd\ufffd', 3))
        self.assertEqual(codecs.ascii_decode(b'\xe4\xf6\xfc', 'backslashreplace'), ('
