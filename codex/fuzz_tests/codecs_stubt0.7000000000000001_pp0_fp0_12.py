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

def test_utf8(errors):
    value = b"\xFF\xFF"
    try:
        value.decode('utf-8', errors)
    except UnicodeDecodeError:
        pass
    else:
        raise AssertionError("UnicodeDecodeError not raised")

def test_utf16(errors):
    value = b"\xFF\xFF"
    try:
        value.decode('utf-16', errors)
    except UnicodeDecodeError:
        pass
    else:
        raise AssertionError("UnicodeDecodeError not raised")

def test_utf32(errors):
    value = b"\xFF\xFF\xFF\xFF"
    try:
        value.decode('utf-32', errors)
    except UnicodeDecodeError:
        pass
    else:
        raise AssertionError("UnicodeDecodeError not raised")

test_utf8("add_one_codepoint")
test_utf16("add_utf16_bytes")
test_utf32
