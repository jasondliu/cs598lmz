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

    def test_utf8_decoder(self):
        d = codecs.getincrementaldecoder("utf-8")()
        assert d.decode(b"", False) == ""
        assert d.decode(b"", True) == ""
        assert d.decode(b"\x80", False) == "�"
        assert d.decode(b"\x80", True) == "�"
        assert d.decode(b"\xc0\x80", False) == "\uDC80"
        assert d.decode(b"\xc0\x80", True) == "\uDC80"
        assert d.decode(b"\xc2\x80", False) == "\uDC80"
        assert d.decode(b"\xc2\x80", True) == "\uDC80"
        assert d.decode(b"\xe0\x80\x80", False) == "\uDC00"
        assert d.decode(b"\xe0\x80\
