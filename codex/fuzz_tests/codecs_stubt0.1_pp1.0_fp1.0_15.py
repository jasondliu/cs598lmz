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
            s.decode("utf-8", "add_one_codepoint")
        except UnicodeDecodeError:
            continue
        try:
            s.decode("utf-8", "add_utf16_bytes")
        except UnicodeDecodeError:
            continue
        try:
            s.decode("utf-8", "add_utf32_bytes")
        except UnicodeDecodeError:
            continue
        print("Failed to raise UnicodeDecodeError for UTF-8 codepoint %x" % i)

    # Test UTF-16
    for i in range(0xD800, 0xE000):
        try:
            s = chr(i).encode
