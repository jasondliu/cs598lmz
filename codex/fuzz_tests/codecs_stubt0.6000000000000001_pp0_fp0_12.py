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

def test_decode_errors():
    for encoding in ('utf-8', 'utf-16-be', 'utf-16-le', 'utf-32-be',
                     'utf-32-le'):
        assert '\ufffd' == codecs.decode(b'\x80', encoding,
                                         'replace').decode(encoding)
        assert '\ufffd\ufffd' == codecs.decode(b'\x80\x80', encoding,
                                               'replace').decode(encoding)
        assert '\ufffd' == codecs.decode(b'\x80', encoding,
                                         'add_one_codepoint').decode(encoding)
        assert '\ufffd\ufffd' == codecs.decode(b'\x80\x80', encoding,
                                               'add_one_codepoint').decode(encoding)
        if encoding in ('utf-16-be', 'utf-16-le'):
            assert '\ufffd' == codecs.decode(b'\
