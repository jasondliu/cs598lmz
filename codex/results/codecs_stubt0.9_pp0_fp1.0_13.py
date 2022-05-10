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

def sjis_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (b'ab', exc.start)
    elif isinstance(exc, UnicodeDecodeError):
        return ("a", exc.start)
    else:
        raise TypeError("don't know how to handle %s" % exc.__name__)

codecs.register_error("sjis_error", sjis_error)


unicode_tests = [
        ('\x00\x7f',
         '\x00\x7f',
         '\u0000\u007f'),
        ('\x81\x9f\xe0\xfc',
         '\xff\x80\x81\x81\xff\x9f\xff\xfd\x8e\xa9\x8e\xa9\xff\xfe',
         '\uFF80\uFF81\uFF9F\uFFFD\u65E5\u65E5'),
        ('\x81\x9f\xe0
