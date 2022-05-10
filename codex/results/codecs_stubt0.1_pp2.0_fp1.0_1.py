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
            continue
        try:
            s.decode("utf-8")
        except UnicodeDecodeError:
            continue
        try:
            s.decode("utf-8", "strict")
        except UnicodeDecodeError:
            continue
        try:
            s.decode("utf-8", "replace")
        except UnicodeDecodeError:
            continue
        try:
            s.decode("utf-8", "ignore")
        except UnicodeDecodeError:
            continue
        try:
            s.decode("utf-8", "add_one_codepoint")
        except UnicodeDecodeError:
            continue
        try:
            s.decode("utf-8", "add_utf16_bytes")
        except UnicodeDecodeError:
            continue
        try:
            s.decode
