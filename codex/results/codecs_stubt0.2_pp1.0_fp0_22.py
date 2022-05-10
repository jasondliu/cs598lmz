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
    # test the error callback mechanism
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            for input in ('\xff', '\xff\xff', '\xff\xff\xff', '\xff\xff\xff\xff'):
                try:
                    input.encode(encoding, errors)
                except UnicodeEncodeError:
                    pass
                else:
                    raise TestFailed("%s/%s didn't raise UnicodeEncodeError" %
                                     (encoding, errors))

    # test the backslashreplace error handler
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for input in ('\xff', '\xff\xff', '\xff\xff\xff', '\xff\xff\xff\xff'):
            output = input.encode(encoding, 'backsl
