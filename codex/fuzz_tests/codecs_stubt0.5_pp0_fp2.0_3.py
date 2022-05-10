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

class TestUnicode:
    def test_decode(self):
        assert u"abc\u1234\u0000\uFFFF".encode("utf-8", "strict") == b"abc\xe1\x88\xb4\x00\xef\xbf\xbf"
        assert u"abc\u1234\u0000\uFFFF".encode("utf-8", "ignore") == b"abc\xe1\x88\xb4\xef\xbf\xbf"
        assert u"abc\u1234\u0000\uFFFF".encode("utf-8", "replace") == b"abc\xe1\x88\xb4\xef\xbf\xbd\xef\xbf\xbd"
        assert u"abc\u1234\u0000\uFFFF".encode("utf-8", "add_one_codepoint") == b"abca\xe1\x88\xb4\x00\xef\xbf\xbf"
        assert u"abc\u1234\u0000\
