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

def test_main():
    with support.check_warnings(("", DeprecationWarning)):
        assert UnicodeEncodeError("ascii", "", 0, 1, "ouch").start == 0
        assert UnicodeDecodeError("ascii", b"", 0, 1, "ouch").start == 0
        assert UnicodeTranslateError("", 0, 1, "ouch").start == 0
        assert UnicodeEncodeError("ascii", "", 0, 1, "ouch").end == 1
        assert UnicodeDecodeError("ascii", b"", 0, 1, "ouch").end == 1
        assert UnicodeTranslateError("", 0, 1, "ouch").end == 1
        assert UnicodeEncodeError("ascii", "", 0, 1, "ouch").reason == "ouch"
        assert UnicodeDecodeError("ascii", b"", 0, 1, "ouch").reason == "ouch"
        assert UnicodeTranslateError("", 0, 1, "ouch").reason == "ouch"
        assert UnicodeEncodeError("ascii", "", 0, 1, "ouch
