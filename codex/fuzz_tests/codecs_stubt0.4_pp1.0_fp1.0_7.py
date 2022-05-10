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

def check_utf16_decode(utf16_bytes, expected_unicode_string, expected_utf16_bytes_consumed):
    utf16_bytes_consumed = 0
    unicode_string = ""
    while utf16_bytes_consumed < len(utf16_bytes):
        unicode_string += utf16_bytes[utf16_bytes_consumed:].decode("utf-16", "add_utf16_bytes")
        utf16_bytes_consumed += 2
    assert unicode_string == expected_unicode_string
    assert utf16_bytes_consumed == expected_utf16_bytes_consumed

def check_utf32_decode(utf32_bytes, expected_unicode_string, expected_utf32_bytes_consumed):
    utf32_bytes_consumed = 0
    unicode_string = ""
    while utf32_bytes_consumed < len(utf32_bytes):
        unicode_string += utf32_bytes[utf32_bytes_consumed:].decode("utf-
