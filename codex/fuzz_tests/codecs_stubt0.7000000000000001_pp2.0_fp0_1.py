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

def test_decode_error_handling(encoding):
    class MyDecodeError(UnicodeDecodeError):
        def __init__(self, encoding, obj, start, end, reason):
            self.encoding = encoding
            self.object = obj
            self.start = start
            self.end = end
            self.reason = reason

        def __str__(self):
            return "decode error for %s" % self.encoding

    def raise_decode_error(exc):
        if isinstance(exc, UnicodeDecodeError):
            raise MyDecodeError(encoding, exc.object, exc.start, exc.end,
                                exc.reason)
        else:
            raise TypeError("don't know how to handle %r" % exc)

    codecs.register_error("raise_decode_error", raise_decode_error)

    try:
        codecs.decode(b'abc', encoding, 'raise_decode_error')
    except MyDecodeError:
        pass
    else:
        raise
