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
    with support.check_warnings(('', UnicodeWarning)):
        for encoding in 'utf-8', 'utf-16', 'utf-32':
            for bad_bytes in (b'\xff', b'\xff\xff', b'\xff\xff\xff'):
                for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint',
                               'add_utf16_bytes', 'add_utf32_bytes'):
                    print(encoding, bad_bytes, errors)
                    s = bad_bytes.decode(encoding, errors)
                    print(s)
                    assert isinstance(s, str)
                    assert len(s) == len(bad_bytes)

    # make sure the surrogatepass error handler works with surrogates
    s = '\udc80'.encode('utf-16-be', 'surrogatepass')
    assert s == b'\x80\xdc'
    s = '\udc80'.encode('utf-16-le', 'surrogatepass')

