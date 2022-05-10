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
    # Test decoding
    assert codecs.charmap_decode(b"abc", "strict", {ord(b"a"): None}) == (
        None, 1)
    assert codecs.charmap_decode(b"abc", "replace", {ord(b"a"): None}) == (
        b"\ufffdbc", 1)
    assert codecs.charmap_decode(b"abc", "ignore", {ord(b"a"): None}) == (
        b"bc", 1)
    assert codecs.charmap_decode(b"abc", "add_one_codepoint", {ord(b"a"): None}) == (
        b"abc", 1)
    assert codecs.charmap_decode(b"abc", "add_utf16_bytes", {ord(b"a"): None}) == (
        b"abc", 1)
    assert codecs.charmap_decode(b"abc", "add_utf32_bytes", {ord(b"
