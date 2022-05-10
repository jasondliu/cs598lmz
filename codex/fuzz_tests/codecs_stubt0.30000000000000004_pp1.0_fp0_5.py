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

# Test the UTF-8 codec

def test_utf8(do_decode):
    # Test decoding of incomplete characters
    assert do_decode(b'\xc3', "utf-8", "replace") == ('\ufffd', 1)
    assert do_decode(b'\xc3x', "utf-8", "replace") == ('\ufffdx', 1)
    assert do_decode(b'\xc3\xc2', "utf-8", "replace") == ('\ufffd\ufffd', 1)
    assert do_decode(b'\xc3\xc2x', "utf-8", "replace") == ('\ufffd\ufffdx', 1)
    assert do_decode(b'\xc3\xc2\xc2', "utf-8", "replace") == ('\ufffd\ufffd\ufffd', 1)
    assert do_decode(b'\xc3\xc2\xc2x', "utf-8", "replace") == ('\ufffd\ufffd\ufffdx', 1)
    assert
