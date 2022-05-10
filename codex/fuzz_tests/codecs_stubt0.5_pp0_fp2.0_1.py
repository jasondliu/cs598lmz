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

def test_decode_utf8(utf8_decoder, utf8_string, utf8_bytes,
                     utf8_string_with_errors, utf8_bytes_with_errors,
                     utf8_string_with_errors_and_replacement,
                     utf8_bytes_with_errors_and_replacement,
                     utf8_string_with_errors_and_xmlcharrefreplace,
                     utf8_bytes_with_errors_and_xmlcharrefreplace,
                     utf8_string_with_errors_and_backslashreplace,
                     utf8_bytes_with_errors_and_backslashreplace,
                     utf8_string_with_errors_and_namereplace,
                     utf8_bytes_with_errors_and_namereplace):
    assert utf8_decoder.decode(utf8_bytes) == utf8_string
    assert utf8_decoder.decode(utf8_bytes_with_errors) == utf8_string_with_errors
    assert ut
