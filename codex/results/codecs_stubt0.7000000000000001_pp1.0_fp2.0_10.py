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

# Test utf-16
def test_utf16_decode():
    assert "ab" == "a".encode("utf-16", "add_one_codepoint").decode("utf-16")
    assert "ab" == "a".encode("utf-16-be", "add_one_codepoint").decode("utf-16-be")
    assert "ab" == "a".encode("utf-16-le", "add_one_codepoint").decode("utf-16-le")
    assert "ab" == "".encode("utf-16", "add_utf16_bytes").decode("utf-16")
    assert "ab" == "".encode("utf-16-be", "add_utf16_bytes").decode("utf-16-be")
    assert "ab" == "".encode("utf-16-le", "add_utf16_bytes").decode("utf-16-le")

def test_utf16_encode():
    assert "ab" == "a".encode("utf-16", "
