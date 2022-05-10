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

def test_utf8_decode_errors():
    # test surrogatepass error handler
    for encoding in ('utf-8', 'utf-8-sig'):
        for data in [b'\xed\xa0\x80', b'\xed\xb0\x80', b'\xed\xa0\x80\xed\xb0\x80']:
            assert codecs.decode(data, encoding, 'surrogatepass') == \
                   '\udc80' * len(data)

    # test backslashreplace error handler
    for encoding in ('utf-8', 'utf-8-sig'):
        for data in [b'\xed\xa0\x80', b'\xed\xb0\x80', b'\xed\xa0\x80\xed\xb0\x80']:
            assert codecs.decode(data, encoding, 'backslashreplace') == \
                   '\\udc80' * len(data)

    # test xmlcharrefreplace error handler
    for encoding
