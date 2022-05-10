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

class CodecTest:
    def test_replace(self, encoding, input, expected, error="replace"):
        self._test(encoding, input, expected, error=error)

    def test_ignore(self, encoding, input, expected):
        self._test(encoding, input, expected, error="ignore")

    def test_xmlcharrefreplace(self, encoding, input, expected):
        self._test(encoding, input, expected, error="xmlcharrefreplace")

    def test_add_one_codepoint(self, encoding, input, expected):
        self._test(encoding, input, expected, error="add_one_codepoint")

    def test_add_utf16_bytes(self, encoding, input, expected):
        self._test(encoding, input, expected, error="add_utf16_bytes")

    def test_add_utf32_bytes(self, encoding, input, expected):
        self._test(encoding, input, expected, error="add_utf32_bytes")

    def test_unicode_escape(self, encoding,
