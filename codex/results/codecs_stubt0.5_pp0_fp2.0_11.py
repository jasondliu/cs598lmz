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
    # Test UTF-8
    for i in range(0xD800, 0xE000):
        try:
            s = chr(i).encode("utf-8")
        except UnicodeEncodeError:
            pass
        else:
            raise TestFailed("Surrogate character %x should not be encodable to UTF-8" % i)

    for i in range(0xD800, 0xE000):
        try:
            s = chr(i).encode("utf-8", "replace")
        except UnicodeEncodeError:
            raise TestFailed("Surrogate character %x should be encodable to UTF-8 with 'replace'" % i)
        if s != b'?':
            raise TestFailed("Surrogate character %x should be encoded to '?' by 'replace', got %r" % (i, s))

    for i in range(0xD800, 0xE000):
        try:
            s = chr(i).encode("utf-8", "backslashreplace")
