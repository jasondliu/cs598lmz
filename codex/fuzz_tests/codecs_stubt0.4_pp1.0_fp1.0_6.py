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
    test_unicode_internal_encode()
    test_unicode_internal_decode()

def test_unicode_internal_encode():
    # test internal unicode to utf-8 encoder
    u = chr(0xdc00)
    try:
        u.encode("utf-8")
    except UnicodeEncodeError as exc:
        assert exc.object is u
        assert exc.encoding == "utf-8"
        assert exc.start == 0
        assert exc.end == 1
        assert exc.reason == "invalid continuation byte"
        assert exc.object[exc.start:exc.end] == u
        assert exc.args == (u, 0, 1, "invalid continuation byte")
    else:
        assert False, "UnicodeEncodeError not raised"

    u = chr(0xd800)
    try:
        u.encode("utf-8")
    except UnicodeEncodeError as exc:
        assert exc.object is u
        assert exc.encoding == "utf
