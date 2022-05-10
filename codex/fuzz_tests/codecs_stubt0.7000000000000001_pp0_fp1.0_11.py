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

def test_decoder_unicodedecodeerror():
    # These are the official tests from PEP 383
    # http://www.python.org/dev/peps/pep-0383/
    import _testcapi
    # "ab" + "\xbd\xb2\x3d\xbc\x20\xe2\x8c\x98"
    s = "ab\xbd\xb2=\xbc ⌘"

    # UTF-8
    for i in range(len(s)+1):
        for j in range(i, len(s)+1):
            for t in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                      'add_utf16_bytes', 'add_utf32_bytes'):
                u = s[i:j].encode('utf-8')
                try:
                    txt = _testcapi.str_from_utf8(u, t, len(u))
                    #print t, i, j, txt
                except UnicodeDecodeError as e:

