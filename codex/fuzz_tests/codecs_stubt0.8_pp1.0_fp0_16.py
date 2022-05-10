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

class AddOneCodepointTest(unittest.TestCase):
    def test_add_one_codepoint(self):
        # UTF-8
        self.assertEqual(codecs.decode("\xc3\x28", "utf-8", "add_one_codepoint"), u"\ufffd(a")

        # UTF-16-LE
        self.assertEqual(codecs.decode("\x28\x00", "utf-16-le", "add_one_codepoint"), u"\ufffd(a")
        self.assertEqual(codecs.decode("\x00\x28", "utf-16-le", "add_one_codepoint"), u"\ufffd\ufffd(a")

        # UTF-16-BE
        self.assertEqual(codecs.decode("\x00\x28", "utf-16-be", "add_one_codepoint"), u"\ufffd(a")
        self.assertEqual(codecs.decode("\
