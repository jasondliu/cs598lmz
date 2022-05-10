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

    def test_register(self):
        # test codecs.register()
        # XXX This test is not complete!

        # test registration of search functions
        f = lambda name, enc=None: 42
        self.assertRaises(TypeError, codecs.register, f)
        self.assertRaises(TypeError, codecs.register, f, 42)
        codecs.register(f)
        self.assertRaises(TypeError, codecs.register, f)
        codecs.register(f)
        codecs.register(f, 'test.unicode_internal_encode')
        self.assertRaises(TypeError, codecs.register, f, 'test.unicode_internal_encode')
        self.assertRaises(TypeError, codecs.register, f, 42)
        self.assertRaises(TypeError, codecs.register, f, 'test.unicode_internal_encode', 42)
        codecs.register(f, 'test.unicode_internal_en
