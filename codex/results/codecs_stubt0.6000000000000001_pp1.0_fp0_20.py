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
        self.assertRaises(TypeError, codecs.register_error, 'strict')
        self.assertRaises(TypeError, codecs.register_error, 'surrogateescape', 'foo')

    def test_strict(self):
        self.assertRaises(UnicodeDecodeError, codecs.decode, b'abc\xff', 'ascii', 'strict')

    def test_ignore(self):
        self.assertEqual(codecs.decode(b'abc\xff', 'ascii', 'ignore'),
                         "abc")

    def test_replace(self):
        self.assertEqual(codecs.decode(b'abc\xff', 'ascii', 'replace'),
                         "abc?")

    def test_backslashreplace(self):
        self.assertEqual(codecs.decode(b'abc\xff', 'ascii', 'backslashreplace'),
                         "
