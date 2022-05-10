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

for encoding in ('utf-16', 'utf-16-le', 'utf-16-be', 'utf-16-ex'):
    print("Testing", repr(encoding))
    for b in (b'a', b'ab', b'abc', b'abcd'):
        for errors in ('strict', 'replace', 'backslashreplace',
                       'ignore', 'add_one_codepoint', 'add_utf16_bytes'):
            print("  ", repr(b), errors)
            # Check that we can decode from bytes
            s = b.decode(encoding, errors)
            # Check that we can encode to bytes
            b2 = s.encode(encoding, errors)
            # Make sure the decoded string is correct
            if errors == 'strict':
                if len(b) % 2 != 0:
                    assert_raises(UnicodeDecodeError, s.decode,
                                  encoding, errors)
                else:
                    assert_raises(UnicodeEncodeError, s.encode,
                                  encoding,
