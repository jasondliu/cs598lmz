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

def check_error_handling(encoding, errors, expected):
    u = u'\u3042\u3044\u3046'
    s = u.encode(encoding, errors)
    u2 = s.decode(encoding, errors)
    if u2 != expected:
        raise ValueError("%s != %s" % (u2, expected))

def test_utf8_error_handling():
    check_error_handling("utf-8", "strict", u'\u3042\u3044\u3046')
    check_error_handling("utf-8", "ignore", u'\u3042\u3044\u3046')
    check_error_handling("utf-8", "replace", u'\u3042\ufffd\u3046')
    check_error_handling("utf-8", "add_one_codepoint", u'\u3042\u3044\u3046')
    check_error_handling("utf-8", "add_utf16_bytes
