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
# In these test, the byte string starts with a byte sequence
# that can be decoded to one character only. If a character
# is added with that byte sequence by the error handler, the
# byte sequences of the following characters will now map to a
# different string of Unicode characters, and they will be
# added to the output.
#
# See http://bugs.jython.org/issue1312
#

print('add_one_codepoint')
b = b'\xC2'
u = u'\uFFFD' + u'Ã'
print('%r [%s]: %r' % (b, codecs.utf_8_decode(b)[1], u))
u = unicode(b, 'utf-8', 'add_one_codepoint')
print('%r: %r' % (b, u))

print('add_utf16_bytes')
b = b'\x00'
u = u'\uFFFD' + u'\u0000'
print('%r [%s]: %r' % (b
