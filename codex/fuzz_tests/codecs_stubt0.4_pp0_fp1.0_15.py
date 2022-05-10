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

    def test_bug_737473(self):
        self.assertEqual(codecs.encode("\u3042", "euc_jis_2004"), b'\x8e\xa4')
        self.assertEqual(codecs.encode("\u3042", "euc_jisx0213"), b'\x8e\xa4')
        self.assertEqual(codecs.encode("\u3042", "shift_jis_2004"), b'\x82\xa0')
        self.assertEqual(codecs.encode("\u3042", "shift_jisx0213"), b'\x82\xa0')

    def test_bug_737473_2(self):
        self.assertEqual(codecs.encode("\u3042", "iso2022_jp_2004"), b'\x1b$B$"\x1b(B')
        self.assertEqual(codecs.
