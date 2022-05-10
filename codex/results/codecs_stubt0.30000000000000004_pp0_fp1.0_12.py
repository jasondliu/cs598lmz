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

class TestUTF7(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(codecs.utf_7_decode(b'+ABA-'), ('\u00c1', 5))
        self.assertEqual(codecs.utf_7_decode(b'+ABA-', errors='strict'), ('\u00c1', 5))
        self.assertEqual(codecs.utf_7_decode(b'+ABA-', errors='ignore'), ('', 0))
        self.assertEqual(codecs.utf_7_decode(b'+ABA-', errors='replace'), ('\ufffd', 5))
        self.assertEqual(codecs.utf_7_decode(b'+ABA-', errors='xmlcharrefreplace'), ('&#193;', 5))
        self.assertEqual(codecs.utf_7_decode(b'+ABA-', errors='backslashreplace'), ('\\U000000c1', 5))
        self
