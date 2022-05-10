import codecs
# Test codecs.register_error()

# This test is not very good, because it doesn't test that the
# registered error handler is actually called.  But it's better than
# nothing.

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# Test that the error handler is actually registered
assert codecs.lookup_error('test.ignore') is handler

# Test that the error handler is actually used
assert codecs.decode('\xff', 'ascii', 'test.ignore') == u''

# Test that the error handler is actually used
assert codecs.encode(u'\uffff', 'ascii', 'test.ignore') == ''

# Test that the error handler is actually used
assert codecs.escape_encode(u'\uffff')[0] == '\\uffff'

# Test that the error handler is actually used
assert codecs.escape_decode('\\uffff')[0] == u'\uffff'

# Test that the error handler
