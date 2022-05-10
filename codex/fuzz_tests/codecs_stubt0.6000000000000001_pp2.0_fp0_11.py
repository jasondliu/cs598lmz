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

#
#   Test UTF-8 codec

def check_utf8(input, errors, expected):
    got = codecs.utf_8_decode(input, errors)
    if got != expected:
        raise TestFailed("decoding '%s' with '%s' failed"
                         " (got %s, expected %s)" %
                         (repr(input), errors, got, expected))
    if errors != "strict":
        s, size = codecs.utf_8_encode(got[0], errors)
        if s != input:
            raise TestFailed("encoding %s with '%s' failed"
                             " (got %s, expected %s)" %
                             (got[0], errors, repr(s), repr(input)))

def encode_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u"\ufffd", exc.start + 1)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def test_utf8():
   
