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

# See http://bugs.python.org/issue19502

iso_8859_15 = 'iso8859_15'
utf_16 = 'utf_16'
utf_32 = 'utf_32'

def test(encoding):
    for name in dir(codecs):
        if not name.startswith("encode_"):
            continue
        func = getattr(codecs, name)
        try:
            func("a", encoding, 'replace')
        except UnicodeEncodeError:
            continue
        try:
            func("a", encoding, 'xmlcharrefreplace')
        except UnicodeEncodeError:
            continue
        func("a", encoding, 'add_one_codepoint')

for encoding in [iso_8859_15, utf_16, utf_32]:
    test(encoding)
