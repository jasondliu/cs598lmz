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

# This test is not exhaustive, but it exercises the most important
# parts of the error handling machinery.

def test_utf8_decode_error_handling():
    # Invalid bytes
    assert u'\ufffd'.encode('utf-8', 'replace') == b'\xef\xbf\xbd'
    assert u'\ufffd\ufffd'.encode('utf-8', 'replace') == b'\xef\xbf\xbd\xef\xbf\xbd'
    assert u'\ufffd'.encode('utf-8', 'ignore') == b''
    assert u'\ufffd'.encode('utf-8', 'xmlcharrefreplace') == b'&#65533;'
    assert u'\ufffd'.encode('utf-8', 'backslashreplace') == b'\\ufffd'
    assert u'\ufffd'.encode('utf-8', 'namereplace') == b'\\N{REPLACEMENT CHARACTER}'

    # Missing bytes
    assert u'\u1234'.encode
