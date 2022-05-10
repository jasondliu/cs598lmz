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

def test_encode_decode_errors():
    for enc in ('utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            for s in ('\udce4', '\udce4\udce4', '\udce4\udce4\udce4', '\udce4\udce4\udce4\udce4', '\udce4\udce4\udce4\udce4\udce4'):
                s.encode(enc, errors)
                if enc == 'utf-16':
                    b = s.encode(enc, errors)
                    s2 = b.decode(enc, errors)
                    assert s == s2

def test_decode_errors():
    for enc in ('utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'ignore', 'replace', 'add_
