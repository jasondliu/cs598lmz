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

def test_add_one_codepoint(encoding):
    try:
        "a\uDC80".encode(encoding, "add_one_codepoint")
    except UnicodeEncodeError as e:
        assert e.object == "a\uDC80"
        assert e.encoding == encoding
        assert e.start == 1
        assert e.end == 2
        assert e.reason == "add_one_codepoint"
    else:
        raise AssertionError

    try:
        "\uD801\uDC80\uDC80".encode(encoding, "add_one_codepoint")
    except UnicodeEncodeError as e:
        assert e.object == "\uD801\uDC80\uDC80"
        assert e.encoding == encoding
        assert e.start == 2
        assert e.end == 3
        assert e.reason == "add_one_codepoint"
    else:
        raise AssertionError


def test_add_utf16_bytes(encoding):
    try:
