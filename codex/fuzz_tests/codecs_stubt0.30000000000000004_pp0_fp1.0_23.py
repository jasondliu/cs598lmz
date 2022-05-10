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
    # test the surrogatepass error handler
    for encoding in ('utf-16', 'utf-32'):
        for handler in ('surrogatepass', 'surrogateescape'):
            for input, expected in [
                (b'\x00\x00\x00\x00', '\U00000000'),
                (b'\x00\x00\x00\x00\x00\x00\x00\x00', '\U00000000\U00000000'),
                (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                 '\U00000000\U00000000\U00000000'),
                (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                 '\U00000000\U00000000\U00000000\U00000000'),
                (b'\x00\x00
