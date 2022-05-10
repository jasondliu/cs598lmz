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
    try:
        u"\u1234".encode("utf-8", "add_one_codepoint")
    except UnicodeEncodeError as e:
        assert e.object == u"\u1234"
        assert e.encoding == "utf-8"
        assert e.start == 0
        assert e.end == 1
        assert e.reason == "add_one_codepoint"
        assert e.object[e.start:e.end] == u"\u1234"
        assert e.args == (u'\u1234', 0, 1, 'add_one_codepoint')
    else:
        assert False, "expected exception"

    try:
        u"\u1234".encode("utf-16", "add_utf16_bytes")
    except UnicodeEncodeError as e:
        assert e.object == u"\u1234"
        assert e.encoding == "utf-16"
        assert e.start == 0
        assert e.end == 1
        assert e.
