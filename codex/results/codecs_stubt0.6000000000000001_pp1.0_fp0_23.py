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

def test():
    # Test UTF-8
    s = b"\xed\xa0\x80\xed\xb0\x80\xed\xbf\xbf\xed\xa0\x80"
    u = "\U000d800\U000d800\U0010ffff\U000d800"

    assert s.decode('utf-8', 'replace') == u.replace('\U000d800', '\ufffd')
    assert s.decode('utf-8', 'ignore') == u[:-1]
    assert s.decode('utf-8', 'backslashreplace') == u.replace('\U000d800', '\\U000d800')
    assert s.decode('utf-8', 'xmlcharrefreplace') == u.replace('\U000d800', '&#55296;')
    assert s.decode('utf-8', 'namereplace') == u.replace('\U000d800', '\\U000d800')

    # Test UTF-16 and UTF-32
    s = b"\
