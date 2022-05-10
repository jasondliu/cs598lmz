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

# get the 'add_codepoint' and 'add_utf16_bytes' errors
c1 = codecs.getencoder('test.unicode.errorhandler')
c2 = codecs.getencoder('test.utf16-be.errorhandler')
c3 = codecs.getencoder('test.utf-32.errorhandler')

f = lambda s: s.replace('\\u', '\\U').replace('u\'', 'U\'')

# encode string, replacing surrogates with the 'encode' error callbacks
# behaves like non-specialized 'unicode-escape' codec
def unicode_escape(s):
    e = s.encode('unicode-escape', 'replace')
    return e.decode('ascii', 'backslashreplace').strip()

a1 = f(unicode_escape('abc\uDC00'))

# call the error callbacks with 'surrogateescape' decoding
# behaves like non-specialized 'unicode-escape' codec

e = 'abc\\U0000e000'.encode('utf
