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

checkException(EncodingError, codecs.utf_8_decode, b'\xf9', final=False)
checkException(EncodingError, codecs.utf_8_decode, b'\xfa', final=False)
checkException(EncodingError, codecs.utf_8_decode, b'\xfb', final=False)
checkException(EncodingError, codecs.utf_8_decode, b'\xfc', final=False)
x = 'abc'+chr(0xd800)
checkEqual(codecs.utf_8_encode(x), (b'abc\xed\xa0\x80', 6))
checkEqual(codecs.utf_8_encode(x, "replace")[0], b'abc\xef\xbf\xbd')
checkEqual(codecs.utf_8_encode(x, "xmlcharrefreplace"), (b'abc&#55296;', 9))
checkEqual(codecs.utf_8_encode(x, "backsl
