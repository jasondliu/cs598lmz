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

class TestCodecs:

    def test_utf_7(self):
        # Make sure that UTF-7 codec is present
        assert isinstance(codecs.lookup('utf-7'), codecs.CodecInfo)

    def test_utf_16_le(self):
        # Make sure that UTF-16-LE codec is present
        assert isinstance(codecs.lookup('utf-16-le'), codecs.CodecInfo)

    def test_utf_32_le(self):
        # Make sure that UTF-32-LE codec is present
        assert isinstance(codecs.lookup('utf-32-le'), codecs.CodecInfo)

    def test_utf_16_be(self):
        # Make sure that UTF-16-BE codec is present
        assert isinstance(codecs.lookup('utf-16-be'), codecs.CodecInfo)

    def test_utf_32_be(self):
        # Make sure that UTF-32-BE codec is present
        assert isinstance(codecs.lookup('utf
