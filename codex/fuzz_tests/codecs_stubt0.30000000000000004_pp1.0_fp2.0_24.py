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

def test_main():
    # Test UTF-8
    for encoding in ('utf-8', 'utf_8'):
        for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            for input in (b'\xff', b'\xc0\x80', b'\xc0\xbf', b'\xc1\x80',
                          b'\xdf\xbf', b'\xe0\x80\x80', b'\xe0\x80\xbf',
                          b'\xe0\x81\x80', b'\xef\xbf\xbf', b'\xf0\x80\x80\x80',
                          b'\xf0\x80\x80\xbf', b'\xf0\x80\x81\x80',
                          b'\xf0\x8f\xbf\xbf', b'\xf1\x80\x80\x80
