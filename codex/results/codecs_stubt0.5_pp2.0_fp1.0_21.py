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
    # test the basic codecs
    for encoding in ('utf-8', 'utf-16', 'utf-16-le', 'utf-16-be',
                     'utf-32', 'utf-32-le', 'utf-32-be',
                     'unicode-escape', 'raw-unicode-escape',
                     'unicode-internal', 'latin-1', 'ascii',
                     'mbcs', 'oem'):
        try:
            s = "abc"
            if encoding in ('mbcs', 'oem'):
                s = s.encode(encoding)
            else:
                s = s.encode(encoding).decode(encoding)
        except LookupError:
            pass

    # test the errors
    for encoding in ('utf-8', 'utf-16', 'utf-16-le', 'utf-16-be',
                     'utf-32', 'utf-32-le', 'utf-32-be',
                     'unicode-escape', 'raw-unicode-escape',
                     '
