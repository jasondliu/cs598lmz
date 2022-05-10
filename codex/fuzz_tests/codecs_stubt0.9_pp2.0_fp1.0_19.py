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

'''.format(string.printable)


@pytest.mark.parametrize(
    'err_name, exc_type, strerror',
    [
        ('add_one_codepoint', UnicodeEncodeError, 'add_one_codepoint'),
        ('add_utf16_bytes', UnicodeEncodeError, 'add_utf16_bytes'),
        ('add_utf32_bytes', UnicodeEncodeError, 'add_utf32_bytes'),
        ('add_one_codepoint', UnicodeDecodeError, 'add_one_codepoint'),
        ('add_utf16_bytes', UnicodeDecodeError, 'add_utf16_bytes'),
        ('add_utf32_bytes', UnicodeDecodeError, 'add_utf32_bytes'),
        ('add_one_codepoint', UnicodeTranslateError, 'add_one_codepoint'),
        ('add_utf16_bytes', UnicodeTranslateError, 'add_utf16_bytes'),
        ('add_utf32_bytes', UnicodeTranslateError, 'add_utf32_bytes'),
