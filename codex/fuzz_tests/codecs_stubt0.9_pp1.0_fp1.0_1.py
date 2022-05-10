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

utf16_data = (
    (b'Hi!'), # no surrogates
    (b'\xFF\xFE\x00\x48\x00\x00\x00\x45\x00\x00\x00\x51'), # UCS-4
    (b'\xFF\xFE\x00\x48\x00\x00\x00\x45\x00\x00\xD8\x51\x00\xDC\x01'), # UCS-4 split into a surrogates
    (b'\xFF\xFE\x00\x48\x00\x00\x00\x45\x00\x00\xD8\x51\x00\xDC\x474',
     b'6\x00\x00\x00\x41\x00\x00\x00\x41\x00\x00\x00\x51'), # UCS-4 split into two surrogates
    # With surrogates
    (b'\xFF\xFE\xD8\x00\
