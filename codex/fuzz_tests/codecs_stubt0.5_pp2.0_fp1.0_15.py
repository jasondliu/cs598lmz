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

def add_one_codepoint_strict(exc):
    if isinstance(exc, UnicodeEncodeError):
        return ("a", exc.start+1)
    elif isinstance(exc, UnicodeDecodeError):
        return ("a", exc.start)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def add_utf16_bytes_strict(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (b'ab', exc.start+1)
    elif isinstance(exc, UnicodeDecodeError):
        return (b'ab', exc.start)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def add_utf32_bytes_strict(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (b'abcd', exc.start+1)
    elif isinstance(exc, UnicodeDecodeError):
        return (b'abcd', exc.start)
    else:
        raise Type
