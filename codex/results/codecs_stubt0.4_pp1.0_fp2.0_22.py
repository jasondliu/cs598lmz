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
    # Test UTF-8
    try:
        s.decode('utf-8')
    except UnicodeDecodeError as exc:
        # Test 'replace'
        s.decode('utf-8', 'replace')
        # Test 'ignore'
        s.decode('utf-8', 'ignore')
        # Test 'backslashreplace'
        s.decode('utf-8', 'backslashreplace')
        # Test 'xmlcharrefreplace'
        s.decode('utf-8', 'xmlcharrefreplace')
        # Test 'add_one_codepoint'
        s.decode('utf-8', 'add_one_codepoint')
        # Test 'surrogateescape'
        s.decode('utf-8', 'surrogateescape')

def test_utf16(s):
    # Test UTF-16-LE
    try:
        s.decode('utf-16-le')
    except UnicodeDecodeError as exc:
        # Test 'replace'
        s.
