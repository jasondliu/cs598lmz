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

def message_string(msg):
    if isinstance(msg, str):
        return msg
    assert isinstance(msg, tuple)
    if len(msg) == 1:
        signature = "a"
    elif len(msg) == 2:
        signature = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuut"
    else:
        raise AssertionError(msg)
    return struct.unpack(signature, msg)[0]

def utf16_exception_ascii(s):
    """utf_16_exception_encode raises a TypeError if passed non-ASCII strings,
    with a surrogateescape-encoded string as part of the message for coverage
    purposes.

    This function returns the surrogateescape-encoded version of the string
    (which also works for ASCII strings, but that's not surprising).
    """
    s_utf8 = s.encode('utf-8', 'surrogateescape')
    for i in range(0, len(s_utf
