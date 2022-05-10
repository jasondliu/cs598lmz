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
    # test utf-16 decoder
    for encoding in ('utf-16', 'utf-16-le', 'utf-16-be'):
        for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint', 'add_utf16_bytes'):
            for data in ('\xff', '\xff\xff', '\xff\xff\xff', '\xff\xff\xff\xff'):
                try:
                    codecs.decode(data, encoding, errors)
                except UnicodeDecodeError as exc:
                    if errors == 'strict':
                        pass
                    elif errors == 'ignore':
                        if encoding in ('utf-16', 'utf-16-le'):
                            assert exc.end == 1
                        elif encoding == 'utf-16-be':
                            assert exc.end == 2
                    elif errors == 'replace':
                        if encoding in ('utf-16', 'utf-16-le'):
                            assert exc.end == 1
                            assert exc.object == '\ufffd
