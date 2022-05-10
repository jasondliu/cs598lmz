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
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                       'surrogateescape', 'surrogatepass', 'backslashreplace'):
            for input in (b'\xff', b'\xff\xff', b'\xff\xff\xff',
                          b'\xff\xff\xff\xff', b'\xff\xff\xff\xff\xff'):
                try:
                    codecs.decode(input, encoding, errors)
                except UnicodeDecodeError as exc:
                    if errors == 'strict':
                        pass
                    elif errors == 'replace':
                        assert exc.object == input
                        assert exc.start == 0
                        assert exc.end == len(input)
                        assert exc.reason == 'invalid start byte'
                        assert exc.encoding == encoding
                    elif errors == 'ignore':
                        assert exc.object == input
                        assert exc.start == 0
                       
