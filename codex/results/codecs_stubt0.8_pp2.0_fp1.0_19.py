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

tests = [
    # ISO-8859-1 (Latin 1)
    ("\xe7", "ISO-8859-1", "strict", u'\xe7'),
    ("\xe7", "ISO-8859-1", "replace", u'\xe7'),
    ("\xe7", "ISO-8859-1", "ignore", u''),
    ("\xe7", "ISO-8859-1", "add_one_codepoint", u'a\xe7'),
    ("\xe7", "ISO-8859-1", "add_utf16_bytes", u'ab\xe7'),
    ("\xe7", "ISO-8859-1", "add_utf32_bytes", u'abcd\xe7'),
    ("\xf7", "ISO-8859-1", "strict", u'\uFFFD'),
    ("\xf7", "ISO-8859-1", "replace", u'?'),
    ("\xf7", "ISO-8859-1", "ignore", u''),
    ("\xf7
