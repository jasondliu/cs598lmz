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

def test_decode(encoding):
    for errors in ["strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
        for input in [b'\x80', b'\x80\x80', b'\x80\x80\x80', b'\x80\x80\x80\x80']:
            decoded = input.decode(encoding, errors=errors)
            encoded = decoded.encode(encoding, errors=errors)
            assert encoded == input


def test_encode(encoding):
    for errors in ["strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
        for input in ["\u0080", "\u0080\u0080", "\u0080\u0080\u0080", "\u0080\u0080\u0080\u0080"]:
            encoded = input.encode(encoding
