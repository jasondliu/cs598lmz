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

def test_unicode_error():
    # Test UnicodeError
    e = UnicodeError("test")
    assert e.reason == "test"
    assert e.object is None
    assert e.start is None
    assert e.end is None
    assert e.encoding is None
    assert e.args == ("test",)

    e = UnicodeError("test", "object", 1, 2, "encoding")
    assert e.reason == "test"
    assert e.object == "object"
    assert e.start == 1
    assert e.end == 2
    assert e.encoding == "encoding"
    assert e.args == ("test", "object", 1, 2, "encoding")

    e = UnicodeError("test", "object", 1, 2, "encoding", "reason")
    assert e.reason == "reason"
    assert e.object == "object"
    assert e.start == 1
    assert e.end == 2
    assert e.encoding == "encoding"
    assert e.args == ("test", "object", 1, 2
