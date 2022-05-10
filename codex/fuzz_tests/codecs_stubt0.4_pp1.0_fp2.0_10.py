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

def test_utf8(s):
    print("utf8:")
    print(s.encode('utf-8'))
    print(s.encode('utf-8', 'replace'))
    print(s.encode('utf-8', 'ignore'))
    print(s.encode('utf-8', 'backslashreplace'))
    print(s.encode('utf-8', 'xmlcharrefreplace'))
    print(s.encode('utf-8', 'add_one_codepoint'))

def test_utf16(s):
    print("utf16:")
    print(s.encode('utf-16'))
    print(s.encode('utf-16', 'replace'))
    print(s.encode('utf-16', 'ignore'))
    print(s.encode('utf-16', 'backslashreplace'))
    print(s.encode('utf-16', 'xmlcharrefreplace'))
    print(s.encode('utf-16', 'add_utf16_bytes
