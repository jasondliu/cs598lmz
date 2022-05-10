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

class Test_codecs:

    # CPython issue #19941: UTF-16 surrogate escape
    def test_surrogate_escape(self):
        s = b'\xed\xa0\x80\xed\xb0\x80'
        self.assertEqual(s.decode("utf-16-le", "surrogatepass"),
                         "\udc80\udc00")
        self.assertEqual(s.decode("utf-16-be", "surrogatepass"),
                         "\udc80\udc00")
        self.assertEqual(s.decode("utf-16", "surrogatepass"),
                         "\udc80\udc00")

        # Issue #19652: UTF-16 surrogateescape should not apply to
        # non-UTF-16 codecs
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf-8', 'surrogateescape')

    def test_error_callback_API(self):
        # Issue #24665: check that the error callback API is what
