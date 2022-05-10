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

def test_cp1252_errors():
    for code in range(256):
        if code not in range(0x80, 0xA0):
            continue
        try:
            s = chr(code).encode("cp1252")
        except UnicodeEncodeError:
            continue
        try:
            s.decode("cp1252")
        except UnicodeDecodeError:
            continue
        assert False, "error expected for codepoint %d" % code

def test_cp1252_errors_recovery():
    for code in range(256):
        if code not in range(0x80, 0xA0):
            continue
        try:
            s = chr(code).encode("cp1252")
        except UnicodeEncodeError:
            continue
        try:
            s.decode("cp1252", errors="add_one_codepoint")
        except UnicodeDecodeError:
            continue
        assert False, "error expected for codepoint %d" % code

def test_utf16_errors():
    for
