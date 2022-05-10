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
                       'surrogateescape', 'surrogatepass'):
            for s in ('abc', '\u3042', '\U00012345'):
                for b in (b'abc', b'\xe3\x81\x82', b'\xf0\x92\x8d\x85'):
                    for i in range(len(b)):
                        for j in range(i, len(b)):
                            b2 = b[:i] + b[j:]
                            try:
                                s2 = s.encode(encoding, errors)
                            except UnicodeEncodeError:
                                if errors == 'strict':
                                    continue
                                else:
                                    raise
                            if s2 != b2:
                                print(encoding, errors, s, s2, b2)
                
