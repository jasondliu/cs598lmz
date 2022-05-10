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

class TestUtf7(unittest.TestCase):
    def test_utf7(self):
        self.assertEqual(codecs.BOM_UTF7, b'+/v8=')
        self.assertEqual(codecs.BOM_UTF7_OK, b'+/v8-')
        self.assertEqual(codecs.BOM_UTF7_LEN, 5)

        self.assertEqual(codecs.getencoder("utf-7")(b"abc"), (b'+ABA-', 5))
        self.assertEqual(codecs.getencoder("utf-7")(b"abc", "strict"), (b'+ABA-', 5))
        self.assertEqual(codecs.getencoder("utf-7")(b"abc", "replace"), (b'+ABA-', 5))
        self.assertEqual(codecs.getencoder("utf-7")(b"abc", "xmlcharrefreplace"), (b'+ABA-', 5))
