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

# test error handling
def test_error_handling(encoding):
    if encoding.startswith("utf-16"):
        test = b'\x00\x00\x00\x00'
        expected = b'\x00\x00\x00\x00ab'
    elif encoding.startswith("utf-32"):
        test = b'\x00\x00\x00\x00'
        expected = b'\x00\x00\x00\x00abcd'
    else:
        test = b'\x00'
        expected = b'\x00a'

    # strict
    with pytest.raises(UnicodeDecodeError):
        test.decode(encoding)

    # replace
    assert test.decode(encoding, "replace") == "\ufffd"

    # ignore
    assert test.decode(encoding, "ignore") == ""

    # xmlcharrefreplace
    assert test.decode(encoding, "xmlcharrefreplace") == "&#x0;"
