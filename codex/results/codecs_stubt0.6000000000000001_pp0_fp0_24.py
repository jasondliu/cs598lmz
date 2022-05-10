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
    for encoding in 'utf-16', 'utf-32':
        for error_handler, expected in [
            ('strict', 'surrogates not allowed'),
            ('ignore', ''),
            ('replace', ''),
            ('add_one_codepoint', ''),
            ('add_utf16_bytes', 'can\'t decode byte 0xab in position 1: truncated data'),
            ('add_utf32_bytes', 'can\'t decode byte 0xab in position 2: truncated data'),
            ]:
            with open(support.TESTFN, "wb") as fp:
                fp.write(b'\xff\xfe\x00\x00')
                fp.write(b'\x00\x00\x00\x00')
            with open(support.TESTFN, "r", encoding=encoding, errors=error_handler) as fp:
                try:
                    fp.read()
                except UnicodeError as exc:
                    assert exc.reason == expected
                else:
                    if expected
