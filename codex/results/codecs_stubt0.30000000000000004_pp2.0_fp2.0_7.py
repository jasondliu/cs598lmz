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
        self.assertEqual(codecs.BOM_UTF7, b'+')
        self.assertEqual(codecs.BOM_UTF7, codecs.BOM_UTF7.decode('utf-7'))

        self.assertEqual(codecs.BOM_UTF7, codecs.BOM_UTF7.decode('utf-7-sig'))

        self.assertEqual(codecs.BOM_UTF7, codecs.BOM_UTF7.decode('utf-7-sig', 'replace'))
        self.assertEqual(codecs.BOM_UTF7, codecs.BOM_UTF7.decode('utf-7-sig', 'ignore'))
        self.assertEqual(codecs.BOM_UTF7, codecs.BOM_UTF7.decode('utf-7-sig', 'backslashreplace'))
        self.assertEqual(codec
