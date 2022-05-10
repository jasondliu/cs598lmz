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

encodings = [
    'unicode-escape',
    'raw_unicode_escape',
    'unicode_internal',
    'ascii',
    'latin-1',
    'mbcs',
    'utf-7',
    'utf-8',
    'utf-16',
    'utf-16-le',
    'utf-16-be',
    'utf-32',
    'utf-32-le',
    'utf-32-be',
    ]

def raise_unicode_exception(encoding):
    s = u"\u1234"
    s.encode(encoding, 'add_one_codepoint')

def test_unicode_exceptions():
    # verify that codecs raise correct exceptions given encoding errors
    from encodings import aliases
    for encoding in encodings:
        try:
            raise_unicode_exception(encoding)
        except UnicodeEncodeError:
            pass
        except UnicodeDecodeError:
            pass
        except LookupError:
            #
