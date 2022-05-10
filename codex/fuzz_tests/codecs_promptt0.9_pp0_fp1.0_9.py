import codecs
# Test codecs.register_error
# UTF-16 skips every other byte:

s = u'a\0b\0c\0'
u2 = codecs.utf_16_decode(s.encode('utf-16'))[0]
assert u2 == u'abc', u2
import _codecs
# Register the error handler
_codecs.register_error('test.skip_byte', lambda e: (u'\uFFFD', e.start+1))
u3 = codecs.utf_16_decode(s.encode('utf-16'), 'test.skip_byte')[0]
assert u3 == u'\uFFFDabb\uFFFDcc', u3
