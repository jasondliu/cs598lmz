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
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for error_handler in ('strict', 'ignore', 'replace'):
            for input_string in ('\x80', '\x80\x80', '\x80\x80\x80'):
                output_string = input_string.encode(encoding, error_handler)
                assert isinstance(output_string, bytes)
                assert output_string == input_string.encode(encoding)
                assert output_string == input_string.encode(encoding, 'strict')
                assert output_string == input_string.encode(encoding, 'ignore')
                assert output_string == input_string.encode(encoding, 'replace')

        for error_handler in ('add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            for input_string in ('\x80', '\x80\x80', '\x80\x80\x80'):
               
