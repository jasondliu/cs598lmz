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

# *** return a string ***

def str_insert_crlf(exc):
    """Insert \r\n for UnicodeEncodeError"""
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return ("\r\n", exc.start)

def str_replace_with_A(exc):
    """Replace with 'A' for UnicodeEncodeError"""
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return "A", exc.start + 1

def str_replace_with_B(exc):
    """Replace with 'B' for UnicodeEncodeError"""
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return "B", exc.start + 1

def str_replace_with_C(exc):
    """Replace with 'C' for UnicodeEncodeError"""
    if not isinstance
