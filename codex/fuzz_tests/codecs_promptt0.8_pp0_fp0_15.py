import codecs
# Test codecs.register_error

# The "decoding error handler" in this test doesn't do anything
# special, but we need to use a local handler to avoid interfering
# with other test cases.
def handler(exception):
	return (u'', exception.end)
codecs.register_error('test.test_codecs_charmap', handler)

# Test the basic operation
s = 'abc\xFF\u0100def\uFFFF'
u = codecs.charmap_decode(s, 'strict', 'test.test_codecs_charmap')[0]
if u != u'abc\uFFFD\u0100def\uFFFD':
	print('charmap_decode: expected %r, got %r' % (u'abc\uFFFD\u0100def\uFFFD', u))

# Test the 'replace' error handler
u = codecs.charmap_decode(s, 'replace', 'test.test_codecs_charmap')[0]
if u != u'abc\uFFFD\u0100
