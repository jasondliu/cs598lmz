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

# Test decoding with errors
def test_utf16_decode(doctest):
    """
    >>> test_utf16_decode(None)
    >>>

    >>> print(b'ab\xff\xfe\x00\x00cd'.decode("utf-16", "replace"))
    ab�cd
    >>> print(b'ab\xff\xfe\x00\x00cd'.decode("utf-16", "ignore"))
    abcd
    >>> print(b'ab\xff\xfe\x00\x00cd'.decode("utf-16", "xmlcharrefreplace"))
    ab&#65533;cd
    >>> print(b'ab\xff\xfe\x00\x00cd'.decode("utf-16", "strict"))
    Traceback (most recent call last):
    UnicodeDecodeError: 'utf16' codec can't decode byte 0xff in position 2: truncated data
    >>> print(b'ab\xff\xfe\x00\x00cd'.decode("utf-16", "add_one_cod
