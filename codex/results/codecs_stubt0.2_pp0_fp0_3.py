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
        for error_handler in ('strict', 'ignore', 'replace', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            for input_string in ('abc', '\u1234', '\u1234\u5678'):
                try:
                    encoded_string = input_string.encode(encoding, error_handler)
                except UnicodeEncodeError:
                    pass
                else:
                    decoded_string = encoded_string.decode(encoding, error_handler)
                    if decoded_string != input_string:
                        print('Failed:', encoding, error_handler, input_string)
                        print('  encoded:', encoded_string)
                        print('  decoded:', decoded_string)

if __name__ == '__main__':
    test_main()
