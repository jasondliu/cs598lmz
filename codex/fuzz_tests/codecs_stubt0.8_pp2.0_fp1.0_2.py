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

def test(name, s, expected):
    t = codecs.decode(s, name, "add_one_codepoint")
    if t != expected:
        print("decode('%s', '%s', 'add_one_codepoint') -> '%s' expected '%s'"\
              % (s, name, t, expected))
    t = codecs.decode(s, name, "add_utf16_bytes")
    if t != expected:
        print("decode('%s', '%s', 'add_utf16_bytes') -> '%s' expected '%s'"\
              % (s, name, t, expected))
    t = codecs.decode(s, name, "add_utf32_bytes")
    if t != expected:
        print("decode('%s', '%s', 'add_utf32_bytes') -> '%s' expected '%s'"\
              % (s, name, t, expected))

for charset in ['iso-8859-1', 'iso-8859-
