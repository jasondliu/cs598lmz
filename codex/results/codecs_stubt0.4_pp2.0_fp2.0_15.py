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

#
# UTF-16
#

# UTF-16BE

def test_utf_16_be_decode(encoding):
    s = "abcd\uDC80\uDC81\uDC82\uDC83\uDC84\uDC85\uDC86\uDC87\uDC88"
    assert codecs.decode(s.encode("utf-16-be"), encoding) == s

def test_utf_16_be_encode(encoding):
    s = "abcd\uDC80\uDC81\uDC82\uDC83\uDC84\uDC85\uDC86\uDC87\uDC88"
    assert codecs.encode(s, encoding) == s.encode("utf-16-be")

def test_utf_16_be_decode_error(encoding):
    s = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
