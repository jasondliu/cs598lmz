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
