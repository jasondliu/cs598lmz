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
    # Test UTF-16 and UTF-32 codecs
    for encoding in ('utf-16', 'utf-32'):
        # Test decoding
        for error_handler in ('strict', 'ignore', 'replace', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            for byteorder in ('little', 'big'):
                # Test decoding
                for input, expected in (
                    (b'\x00\x00\x00\x00', '\U00000000'),
                    (b'\x00\x00\x00\x01', '\U00000001'),
                    (b'\x00\x00\x00\x7f', '\U0000007f'),
                    (b'\x00\x00\x00\x80', '\U00000080'),
                    (b'\x00\x00\x00\xff', '\U000000ff'),
                    (b'\x00\x00\x01\x00', '\U00000100'),

