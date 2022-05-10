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
    # test surrogatepass
    for encoding in ('utf-16', 'utf-16-le', 'utf-16-be'):
        for errors in ('surrogatepass', 'surrogateescape', 'replace', 'ignore',
                       'add_one_codepoint', 'add_utf16_bytes'):
            for input in (b'\x00\xd8', b'\x00\xdc', b'\xd8\x00', b'\xdc\x00'):
                try:
                    input.decode(encoding, errors)
                except UnicodeDecodeError as exc:
                    if errors == 'surrogatepass':
                        raise
                    if errors == 'surrogateescape':
                        assert exc.object[exc.start] == 0xdc00
                    elif errors == 'replace':
                        assert exc.object[exc.start] == 0xfffd
                    elif errors == 'ignore':
                        assert exc.object[exc.start] == 0x00
                    elif errors == 'add_one_codepoint':

