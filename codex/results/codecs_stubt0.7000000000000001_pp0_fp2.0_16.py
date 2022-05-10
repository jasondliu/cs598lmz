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
    # UTF-8
    assert "\xc3\x28".decode("utf-8", "replace") == "\ufffd(", "replace"
    assert "\xc3\x28".decode("utf-8", "ignore") == "", "ignore"
    assert "\xc3\x28".decode("utf-8", "strict") == u"\ufffd", "strict"
    assert "\xc3\x28".decode("utf-8", "xmlcharrefreplace") == "&#x3c;(", "xmlcharrefreplace"
    assert "\xc3\x28".decode("utf-8", "add_one_codepoint") == "a(", "add_one_codepoint"
    assert "\xc3\x28".decode("utf-8", "backslashreplace") == "\\uC32", "backslashreplace"
    assert "\xc3\xc2\xa9".decode("utf-8", "backslashreplace") == "\\uC3\\uC2A9", "
