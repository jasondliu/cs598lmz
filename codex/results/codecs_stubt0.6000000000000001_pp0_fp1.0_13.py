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
    for encoding in (
            'utf-8', 'utf-16', 'utf-32', 'unicode-internal',
            'idna', 'punycode'):
        for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            print(encoding, errors)
            s = '\x80'
            if encoding in ('utf-16', 'utf-32', 'unicode-internal'):
                s = s.encode('latin-1')
            try:
                s.decode(encoding, errors)
            except UnicodeError as e:
                print("Failed:", e.__class__.__name__, e)
                if errors == 'strict':
                    pass
                elif errors == 'ignore':
                    pass
                elif errors == 'replace':
                    if encoding in ('utf-8', 'utf-16', 'utf-32', 'unicode-internal'):
                        pass
                    else
