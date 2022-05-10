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
    for (input, expected) in [
        (b'\x80', '\uFFFD'),
        (b'\x80\x80', '\uFFFD\uFFFD'),
        (b'\x80\x80\x80', '\uFFFD\uFFFD\uFFFD'),
        (b'\x80\x80\x80\x80', '\uFFFD\uFFFD\uFFFD\uFFFD'),
        (b'\x80\x80\x80\x80\x80', '\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD'),
        (b'\x80\x80\x80\x80\x80\x80', '\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD'),
        (b'\x80\x80\x80\x80\x80\x80\x80', '\uFFFD\uFFFD
