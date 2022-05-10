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
    # test codecs.register_error()

    # test that the error handler is called
    for encoding in ('utf-16', 'utf-32'):
        for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            print("testing", encoding, errors)
            result = codecs.decode(b'\xff', encoding, errors)
            if errors == 'strict':
                assert result == None
            elif errors == 'ignore':
                assert result == ''
            elif errors == 'replace':
                assert result == '\ufffd'
            elif errors == 'add_one_codepoint':
                assert result == 'a'
            elif errors == 'add_utf16_bytes':
                assert result == 'ab'
            elif errors == 'add_utf32_bytes':
                assert result == 'abcd'
            else:
                raise ValueError("unexpected error handler")

    # test that the error
