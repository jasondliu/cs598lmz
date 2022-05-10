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

class TestDecode:
    def test_utf16_be(self):
        s = b"\x00\x61\x00\x62\x00\x63"
        assert s.decode("utf-16-be") == "abc"
        assert s.decode("utf-16-be", "ignore") == ""
        assert s.decode("utf-16-be", "replace") == "\ufffd\ufffd\ufffd"
        assert s.decode("utf-16-be", "add_one_codepoint") == "a\ufffd"
        assert s.decode("utf-16-be", "add_utf16_bytes") == "ab\ufffd"
        assert s.decode("utf-16-be", "add_utf32_bytes") == "ab\ufffd\ufffd"

    def test_utf16_le(self):
        s = b"\x61\x00\x62\x00\x63\x00"
        assert s.decode("utf-16-le") == "abc"
