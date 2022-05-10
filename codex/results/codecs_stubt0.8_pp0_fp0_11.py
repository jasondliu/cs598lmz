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
    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_error,
                          "add_one_codepoint", lambda x: x)
        self.assertRaises(TypeError, codecs.register_error,
                          "add_one_codepoint", add_utf16_bytes)

    def test_utf_32_le(self):
        # Bug 802758: UTF-32 codec should accept and decode
        # BOM and LE/BE marker
        self.assertEqual(u'\ufffd'.encode('utf-32-le'), b'\x00\x00\x00\xff')
        self.assertEqual(u'\ufffd'.encode('utf-32-be'), b'\xff\x00\x00\x00')
        self.assertEqual(b'\x00\x00\x00\xff'.decode('utf-32-le'), u'\ufffd')
        self.assertEqual
