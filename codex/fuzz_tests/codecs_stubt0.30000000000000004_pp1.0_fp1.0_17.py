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
    # Test that UnicodeEncodeError and UnicodeDecodeError objects
    # have the attributes and methods described in the documentation.

    # EncodeError
    e = UnicodeEncodeError("ascii", u"\u3042", 0, 1, "ouch")
    assert e.encoding == "ascii"
    assert e.object == u"\u3042"
    assert e.start == 0
    assert e.end == 1
    assert e.reason == "ouch"
    assert str(e) == "'ascii' codec can't encode character '\u3042' in position 0: ouch"

    # DecodeError
    e = UnicodeDecodeError("ascii", b"\xff", 0, 1, "ouch")
    assert e.encoding == "ascii"
    assert e.object == b"\xff"
    assert e.start == 0
    assert e.end == 1
    assert e.reason == "ouch"
    assert str(e) == "'ascii' codec can't decode byte 0xff in
