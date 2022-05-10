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

    def test_utf7(self):
        self.assertEqual(codecs.utf_7_decode(b"+ABA-"), ("\u00c4\u00e4", 5))
        self.assertEqual(codecs.utf_7_decode(b"+ABA-", errors="ignore"), ("", 5))
        self.assertEqual(codecs.utf_7_decode(b"+ABA-", errors="replace"), ("\ufffd", 5))
        self.assertEqual(codecs.utf_7_decode(b"+ABA-", errors="add_one_codepoint"), ("a\u00c4\u00e4", 5))
        self.assertEqual(codecs.utf_7_decode(b"+ABA-", errors="add_utf16_bytes"), ("\u00c4\u00e4", 5))
        self.assertEqual(codecs.utf_7_decode(b
