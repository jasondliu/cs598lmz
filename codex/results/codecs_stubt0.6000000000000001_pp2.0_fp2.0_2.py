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
    # Make sure the codecs module can be imported
    import codecs

    # Test utf-8 codec
    utf8 = codecs.lookup("utf-8")
    s = u"abc\u20ac\u20ac\u20acdef"
    enc = utf8.encode(s, "strict")[0]
    assert enc == "abc\xe2\x82\xac\xe2\x82\xac\xe2\x82\xacdef"
    assert utf8.decode(enc, "strict") == (s, len(enc))
    s2 = u"abc\ufffd\ufffd\ufffddef"
    assert utf8.decode(enc[:3] + enc[6:], "replace") == (s2, 9)
    assert utf8.decode(enc[:3] + enc[6:], "ignore") == (s2[:3] + s2[6:], 6)
    assert utf8.decode(enc[:
