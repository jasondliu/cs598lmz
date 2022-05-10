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


class TestUTF8:
    def test_str_decoding(self):
        s = b"abc\xed\xa0\x80"
        assert s.decode("utf-8") == "abc\uD800"
        assert s.decode("utf-8", "replace") == "abc?"
        assert s.decode("utf-8", "ignore") == "abc"
        assert s.decode("utf-8", "backslashreplace") == r"abc\ud800"
        assert s.decode("utf-8", "xmlcharrefreplace") == "abc&#65536;"
        assert s.decode("utf-8", "add_one_codepoint") == "abc\uD800a"
        py.test.raises(UnicodeDecodeError, s.decode, "utf-8", "add_utf16_bytes")
        py.test.raises(UnicodeDecodeError, s.decode, "utf-8", "add_utf32_bytes")
        #
        s = b"abc\
