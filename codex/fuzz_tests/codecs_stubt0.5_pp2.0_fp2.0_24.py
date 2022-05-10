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

def test_errorhandler_callable():
    assert codecs.strict_errors(UnicodeEncodeError("ascii", "\xe9", 0, 1, "ouch")) == (u'?', 1)
    assert codecs.ignore_errors(UnicodeEncodeError("ascii", "\xe9", 0, 1, "ouch")) == (u'', 1)
    assert codecs.replace_errors(UnicodeEncodeError("ascii", "\xe9", 0, 1, "ouch")) == (u'?', 1)
    assert codecs.xmlcharrefreplace_errors(UnicodeEncodeError("ascii", "\xe9", 0, 1, "ouch")) == (u'&#233;', 1)
    assert codecs.backslashreplace_errors(UnicodeEncodeError("ascii", "\xe9", 0, 1, "ouch")) == (u'\\xe9', 1)
    assert codecs.add_one_codepoint(UnicodeEncodeError("ascii", "\xe9", 0, 1, "ouch
