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
    tests = [
        ("utf_16_be", "utf_16_be", "\x00a"),
        ("utf_16_le", "utf_16_le", "a\x00"),
        ("utf_32_be", "utf_32_be", "\x00\x00\x00a"),
        ("utf_32_le", "utf_32_le", "a\x00\x00\x00"),
        ("cp1252", "utf_16_be", "\x00a"),
        ("cp1252", "utf_16_le", "a\x00"),
        ("cp1252", "utf_32_be", "\x00\x00\x00a"),
        ("cp1252", "utf_32_le", "a\x00\x00\x00"),
        ("latin-1", "utf_16_be", "\x00a"),
        ("latin-1", "utf_16_le", "a\x00"),
        ("latin-1", "utf_32_be
