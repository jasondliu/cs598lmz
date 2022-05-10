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

codec_tests = [
    # From PEP 383
    ('abc\udcba', 'unicode_escape', 'abc\udcba'),
    ('abc\udcba', 'raw_unicode_escape', 'abc\\udcba'),
    ('abc\udcba', 'unicode_internal', 'abc\\udcba'),
    ('\udcba', 'ascii', '�'),
    ('\udcba', 'ascii', '�', 'replace'),
    ('\udcba', 'ascii', 'a', 'add_one_codepoint'),
    ('\udcba', 'utf-7', '+ADcBA-'),
    ('\udcba', 'utf-8', b'\xed\xb2\xba'),
    ('\udcba', 'utf-16', b'\xdc\xba'),
    ('\udcba', 'utf-16-le', b'\xba\xdc'),
    ('\udcba', 'utf-16-be', b'\xdc\
