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
    # _is_cpython is True if we're running on CPython.
    _is_cpython = hasattr(sys, "gettotalrefcount")

    def test_utf7(self):
        self.assertEqual(codecs.BOM_UTF7, codecs.BOM_UTF7)
        self.assertNotEqual(codecs.BOM_UTF8, codecs.BOM_UTF7)

    def test_utf8_decode(self):
        self.assertEqual(codecs.utf_8_decode(b'abc'), ('abc', 3))
        self.assertEqual(codecs.utf_8_decode(b'\xe4\xbd\xa0\xe5\xa5\xbd'), ('你好', 6))
        self.assertEqual(codecs.utf_8_decode(b'\xf0\x90\x8c\xbc'), ('𐌼', 4))

    def test_utf
