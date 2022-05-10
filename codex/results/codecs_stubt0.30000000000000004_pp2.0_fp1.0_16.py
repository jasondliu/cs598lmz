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
        for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint'):
            for input in ('abc\x80def', 'abc\x80'):
                for start in range(len(input) + 1):
                    for stop in range(start, len(input) + 1):
                        for step in (-1, 1):
                            s = input[start:stop:step]
                            if errors == 'add_one_codepoint':
                                expected = s + 'a'
                            else:
                                expected = s
                            t = codecs.decode(s.encode(encoding), encoding, errors)
                            if t != expected:
                                print('Failed:', encoding, errors, repr(s), start, stop, step, repr(t), repr(expected))

    # Test UTF-16
    for encoding in ('utf-16', 'utf_16'):
        for errors in ('st
