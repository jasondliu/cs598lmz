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

def test_utf8_errors():
    # Test UTF-8 decoding error handlers
    for bad_bytes in [b'\x80', b'\xff', b'\xc0\x80', b'\xc0\xbf', b'\xc1\x80',
                      b'\xc1\xbf', b'\xe0\x80\x80', b'\xe0\x80\xbf',
                      b'\xe0\x81\x80', b'\xe0\x81\xbf', b'\xe0\x9f\xbf',
                      b'\xe0\xa0\x80', b'\xe0\xbf\xbf', b'\xe1\x80\x80',
                      b'\xe1\x80\xbf', b'\xe1\x9f\xbf', b'\xe1\xa0\x80',
                      b'\xe1\xbf\xbf', b'\xec\xbf\xbf', b'\xed\x80\x80',
