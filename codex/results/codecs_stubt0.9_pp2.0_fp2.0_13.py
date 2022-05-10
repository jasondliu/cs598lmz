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

def test_utf16(input, errors, expected_len):
    raw = bytes(input, "utf16")
    got = str(raw, "utf16", errors)
    assert len(got) == expected_len

def test_utf32(input, errors, expected_len):
    raw = bytes(input, "utf32")
    got = str(raw, "utf32", errors)
    assert len(got) == expected_len

unicode_surrogate_pair = "\ud87e\udc01"

char_ab_pairs = [
    b'\x00\xa9',
    b'\x02\xd1',
    b'\x21\x42',
    b'\x5a\xf5',
    b'\xaa\x55',
    b'\xcc\x99',
    b'\xf8\xff',
    b'\xfe\xff',
    b'\xfe\xfe',
    b'\xff\xff',
]

test_utf16(unicode_
